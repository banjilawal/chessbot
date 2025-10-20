# src/chess/piece/event/validation/actor_candidate.py

"""
Module: chess.piece.event.validation.actor_candidate
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.0

"""
from typing import TypeVar, cast, Tuple

from chess.piece.event.validation.actor.exception import CheckMatedKingCannotMoveException, NoInitialPlacementException
from chess.piece.model.piece import CombatantPiece, KingPiece
from chess.square import Square
from chess.system import BindingValidator, LoggingLevelRouter, ValidationResult, Validator
from chess.board import Board, BoardPieceSearch, BoardSquareSearch, BoardSearchContext

from chess.piece import (
  ActorNotOnRosterCannotMoveException, CapturedActorCannotMoveException, Piece, InvalidTravelActorException,
  ActorNotOnBoardCannotMoveException,
  PieceValidator, TravelActorNotFoundException,
  TravelActorSquareNotFoundException, SquareMisMatchesTravelActorException
)

T = TypeVar('T')

"""
Implements the `OccupationExecutor` class, which handles executing event
directives in the chess engine. This includes moving pieces, capturing enemies,
and coordinating rollback logic in case of inconsistencies or failed operations.

Attributes:
  * `OccupationExecutor:` Main class responsible for executing event directives.
  * `_attack_enemy`: Static method for processing attacks on enemy pieces.
  * `_run_scan`: Static method for handling discoveries on occupied squares.
  * `_switch_squares`: Static method the transferring team piece to team different `Square`.
"""
class TravelActorValidator(Validator[Piece]):
  """
  # ROLE: Validator, Data Integrity

  # RESPONSIBILITIES:
  1. Ensure `TravelEvent` actor_candidate has a valid binding to the execution environment for `TravelEventFactory`.
  2. If binding requirements are not satisfied return the appropriate error to `TravelEventFactory` in
      `ValidationResult`.
  3. Discover potential data integrity violations.

  # PROVIDES:
  `ValidationResult`: Return type containing the built `Team` or error information.

  # ATTRIBUTES:
  None
  """

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: T) -> ValidationResult[Piece]:
    """"""
    method = "TravelActorValidator.validate"

    try:
      validation = PieceValidator.validate(candidate)
      if validation.is_failure():
        return ValidationResult(exception=validation.exception)

      actor = cast(Piece, validation.payload)

      # If the piece has no position history its not on the board and cannot piece.
      if actor.current_position is None or actor.positions.is_empty():
        return ValidationResult(exception=NoInitialPlacementException(
          f"{method}: {NoInitialPlacementException.DEFAULT_MESSAGE}"
        ))

      # If the piece is not on its team roster it cannot be a TravelEvent actor_candidate. This might have been
      # checked by the PieceValidator
      team = actor.team
      if actor not in team.roster:
        return ValidationResult(exception=ActorNotOnRosterCannotMoveException(
          f"{method}: {ActorNotOnRosterCannotMoveException.DEFAULT_MESSAGE}"
        ))

      # A captured combatant cannot be a TravelEvent actor_candidate. No need for validating a checkmated
      # king as an actor_candidate because the game ends when a king is in checkmate.
      if isinstance(actor, CombatantPiece) and actor.captor is not None:
        return ValidationResult(exception=CapturedActorCannotMoveException(
          f"{method}: {CapturedActorCannotMoveException.DEFAULT_MESSAGE}"
        ))

      if isinstance(actor, KingPiece):
        king_piece = cast(KingPiece, actor)
        if king_piece.is_checkmated:
          return ValidationResult(exception=CheckMatedKingCannotMoveException(
            f"{method}: {CheckMatedKingCannotMoveException.DEFAULT_MESSAGE}"
          ))

      return ValidationResult(payload=actor)
    except Exception as e:
      return ValidationResult(exception=e)