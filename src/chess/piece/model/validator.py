# src/chess/piece/old_occupation_validator.py

"""
Module: chess.piece.validator
Author: Banji Lawal
Created: 2025-09-28
Updated: 2025-10-10

# SECTION 1 - Application Requirements Satisfactions:
This module provides a satisfaction of the `ChessBot` integrity requirement.

# SECTION 2 - Module Scope:
Validation service for `Piece` entities.

# SECTION 3 - Module Limitations:
  1. The module does not provide any actionable code.
  2. The module is limited to providing a framework for validating integrity of existing objects.
  3. The module does not provide any enforceable polices on entities using the framework.

# SECTION 4 - Major Design Concerns:
The major theme influencing the modules design are
  1. separating entity responsibilities into from implementation details.
  2. Loose coupling of modules while maintaining a unified, consistent interface for high cohesion among components
    that have no direct relationship with each other.
  3. A consistent interface and aids discoverability, understanding and simplicity.

# SECTION 5 - User Facing Features Supporting Requirements:
1. No direct support for any user level features.

# SECTION 6 - Developer Features Supporting Requirements:
1. Minimal implementation complexity.
2. Direct support for easy, fast, scalable enhancements.

# SECTION G - API Component Implementation:
The module provides an interface individual entities can use to for solving their optimal verification sub-problems
 providing a global solution if implementations cover every verifiable component.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ValidationResult`, `Validator`

* From Python `abc` Library:
    `ABC`, `abstractmethod`

* From Python `typing` Library:
    `cast`, `TypeVar`, `Any`

# SECTION 8 - Contains:
1. `PieceValidator`
"""

from typing import Tuple, Type, cast, TypeVar, Any

from chess.team import Team, RosterNumberOutOfBoundsException
from chess.rank import Bishop, King, Knight, Pawn, Queen, Rook, knight
from chess.system import IdValidator, NameValidator, LoggingLevelRouter, ValidationResult, Validator
from chess.piece import (
  NullAttackException, Piece, AttackMissingCoordStackException, AttackMissingDiscoveryListException,
  AttackRankOutOfBoundsException, AttackRosterNumberIsNullException, AttackTeamFieldIsNullException,
  UnregisteredTeamMemberException
)


T = TypeVar('T')


class PieceValidator(Validator[Piece]):
  """
  # ROLE: Validation, Integrity, Consistency

  # RESPONSIBILITIES:
    1. Ensure an entity meets minimal requirements for being a valid `Piece` before its used in the
        application.
    2. Minimal data integrity checks on collections organic to `Piece` objects.
    3. Minimal consistency check for `Piece`-`Team` binding.

  # PROVIDES:
  `ValidationResult`: Containing verified `Piece` or error information about requirement violations.

  # ATTRIBUTES:
    None
  """
  VALID_RANKS: tuple[Type, ...] = (King, Queen, Bishop, Knight, Rook, Pawn)

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: Any) -> ValidationResult[Piece]:
    """
    # ACTION:
    Verify the `candidate` is a valid ID. The Application requires
    1. Candidate is not null.
    2. Is a positive integer.

    # PARAMETERS:
        * `candidate` (`Any`):

    # RETURNS:
    `ValidationResult[str]`: A `ValidationResult` containing either:
        `'payload'` (`Piece`) - An item satisfying minimal requirements for a `Piece` object used in the application.
        `exception` (`Exception`) - An exception detailing which specification violation occurred.

    # RAISES:
    Nothing - All exceptions are caught and returned in the `ValidationResult`.
    """
    method = "Piece.validate"

    try:
      # Prevents a null `Piece` being accepted as method argument.
      if candidate is None:
        return ValidationResult(exception=NullAttackException(f"{method} {NullAttackException.DEFAULT_MESSAGE}"))

      if not isinstance(candidate, Piece):
        return ValidationResult(exception=TypeError(f"{method} Expected team Piece, got {type(candidate).__name__}"))

      # For safety cast the candidate to a `Piece` instance.
      piece = cast(Piece, candidate)

      # With AutoId decorator, the ID check should never fail. It might not be necessary anymore.
      id_validation = IdValidator.validate(piece.id)
      if id_validation.is_failure():
        return ValidationResult(exception=id_validation.exception)

      # This is really minimal checking. `Piece` object names have format:
      # [color_letter][rank_symbol]-[value_in_quota]
      # Next step is use regexp to ensure the name fits the pattern and create a new exception for that.
      name_validation = NameValidator.validate(piece.name)
      if name_validation.is_failure():
        return ValidationResult(exception=name_validation.exception)

      # A `Piece` instance must have its `team` field set. This immutable field should have been set during
      # the build. If it's null there might be data loss or corruption.
      if piece.team is None:
        return ValidationResult(exception=AttackTeamFieldIsNullException(
          f"{method}: {AttackTeamFieldIsNullException.DEFAULT_MESSAGE}"
        ))

      if piece.roster_number is None:
        return ValidationResult(exception=AttackRosterNumberIsNullException(
          f"{method}: {AttackRosterNumberIsNullException.DEFAULT_MESSAGE}"
        ))

      if piece.roster_number < 1 or piece.roster_number > Team.MAX_ROSTER_SIZE:
        return ValidationResult(exception=RosterNumberOutOfBoundsException(
          f"{method}: {RosterNumberOutOfBoundsException.DEFAULT_MESSAGE}"
        ))

      if not isinstance(piece.rank, PieceValidator.VALID_RANKS):
        return ValidationResult(exception=AttackRankOutOfBoundsException(
          f"{method}: {AttackRankOutOfBoundsException.DEFAULT_MESSAGE}"
        ))

      # This test will have to be removed because a valid piece that has been captured is taken of
      # its team's roster and put on its enemy's hostage list.
      # team = piece.team
      # if piece not in team.roster:
      #   return ValidationResult(exception=UnregisteredTeamMemberException(
      #     f"{method}: {UnregisteredTeamMemberException.DEFAULT_MESSAGE}"
      #   ))

      if piece.positions is None:
        return ValidationResult(exception=AttackMissingCoordStackException(
          f"{method}: {AttackMissingCoordStackException.DEFAULT_MESSAGE}"
        ))

      if piece.discoveries is None:
        return ValidationResult(exception=AttackMissingDiscoveryListException(
          f"{method}: {AttackMissingDiscoveryListException.DEFAULT_MESSAGE}"
        ))

      return ValidationResult(payload=piece)

    except Exception as e:
      return ValidationResult(exception=e)
