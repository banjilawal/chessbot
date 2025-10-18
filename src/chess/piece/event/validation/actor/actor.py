# src/chess/piece/event/validation/actor_candidate.py

"""
Module: chess.piece.event.validation.actor_candidate
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.0

"""
from typing import TypeVar, cast, Any

from chess.board.validator import BoardValidator
from chess.square import Square
from chess.system import LoggingLevelRouter, ValidationResult, ActorValidator
from chess.board import Board, BoardPieceSearch, BoardSquareSearch, BoardSearchContext

from chess.piece import (
  Piece, CombatantPiece, PieceValidator, InvalidTravelActorException, ActorNotOnRosterCannotMoveException,
  ActorNotOnBoardCannotMoveException, CapturedActorCannotMoveException, TravelActorNotFoundException,
  TravelActorSquareNotFoundException, NullTravelActorException, SquareMisMatchesTravelActorException,
  ActorBoardConsistencyValidator
)

A = TypeVar("A")
X = TypeVar("X")

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
class TravelActorValidator:
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

  _actor_validator: PieceValidator
  _environment_validator: BoardValidator
  _binding_validator: ActorBoardConsistencyValidator

  def __init__(
    self,
    actor_validator: PieceValidator,
    environment_validator: BoardValidator,
    binding_validator: ActorBoardConsistencyValidator
  ):
    self._actor_validator = actor_validator
    self._environment_validator = environment_validator
    self._binding_validator = binding_validator

  @classmethod
  def create_default(cls) -> 'TravelActorValidator':
    """Factory method for default configuration"""
    return cls(
      actor_validator=PieceValidator(),
      environment_validator=BoardValidator(),
      binding_validator=ActorBoardConsistencyValidator()
    )

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, actor_candidate: Any, environment_candidate: Any) -> ValidationResult[Piece]:
    """"""
    method = "TravelActorValidator.validate"

    try:
      #========= Validate the Board_Candidate =========#
      board_validation = BoardValidator.validate(environment_candidate)
      if board_validation.is_failure():
        return ValidationResult(exception=board_validation.exception)

      # Cast board_validator if validation is successful
      board = cast(board_validation.payload, Board)

      #========= Validate the Actor_Candidate =========#
      # Do standard piece validations first
      piece_validation = PieceValidator.validate(actor_candidate)
      if piece_validation.is_failure():
        return ValidationResult(exception=piece_validation.exception)

      # Cast actor_candidate if validation is successful
      piece = cast(piece_validation.payload, Piece)






      #========= Actor's Square Sanity Checks and  =========#
      """
      Ensure Actor_Candidate is on a square. Checking the position history is not enough because a captured piece 
      will still have a position history but it should not be on the board. A thorough check will see if the piece 
      was in the opposing team's hostages. Doing that will introduce more dependencies. Making sure Actor_Candidate 
      is in the square is a good check.
      """

      # Find the square associated with the piece's last position.
      actor_square_search = BoardSquareSearch.search(
        board=board_validator,
        search_context=BoardSearchContext(coord=actor_candidate.current_position)
      )

      if actor_square_search.is_empty():
        return ValidationResult(exception=TravelActorSquareNotFoundException(
          f"{method}: {TravelActorSquareNotFoundException.DEFAULT_MESSAGE}"
        ))

      if actor_square_search.is_failure():
        return ValidationResult(exception=actor_square_search.exception)

      # Just for safety cast the found square
      square = cast(Square, actor_square_search.payload[0])

      # If the piece is not the square's occupant it cannot be a TravelEvent's actor_candidate. Data inconsistency
      # or some other integrity problem is likely.
      if square.occupant is not piece:
        return ValidationResult(exception=SquareMisMatchesTravelActorException(
          f"{method}: {SquareMisMatchesTravelActorException.DEFAULT_MESSAGE}"
        ))

      return ValidationResult(payload=actor_square_search.payload[0])
    except Exception as e:
      return ValidationResult(exception=InvalidTravelActorException(f"{method}: {e}"))