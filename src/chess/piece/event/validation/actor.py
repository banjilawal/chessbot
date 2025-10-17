# src/chess/piece/event/validation/actor.py

"""
Module: chess.piece.event.validation.actor
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.0

"""
from typing import TypeVar, cast

from chess.board.validator import BoardValidator
from chess.square import Square
from chess.system import LoggingLevelRouter, ValidationResult, ActorValidator
from chess.board import Board, BoardPieceSearch, BoardSquareSearch, BoardSearchContext

from chess.piece import (
  Piece, CombatantPiece, PieceValidator, InvalidTravelActorException, ActorNotOnRosterCannotMoveException,
  ActorNotOnBoardCannotMoveException, CapturedActorCannotMoveException, TravelActorNotFoundException,
  TravelActorSquareNotFoundException, NullTravelActorException, SquareMisMatchesTravelActorException
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
class TravelActorValidator(ActorValidator[Piece, Board, Square]):
  """
  # ROLE: Validator, Data Integrity

  # RESPONSIBILITIES:
  1. Ensure `TravelEvent` actor_candidate has a valid binding to the execution environment for `TravelEventBuilder`.
  2. If binding requirements are not satisfied return the appropriate error to `TravelEventBuilder` in
      `ValidationResult`.
  3. Discover potential data integrity violations.

  # PROVIDES:
  `ValidationResult`: Return type containing the built `Team` or error information.

  # ATTRIBUTES:
  None
  """

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, actor_candidate: A, board_candidate: X) -> ValidationResult[Square]:
    """"""
    method = "TravelActorValidator.validate"

    try:
      #========= Validate the Board_Candidate =========#
      board_validation = BoardValidator.validate(board_candidate)
      if board_validation.is_failure():
        return ValidationResult(exception=board_validation.exception)

      # Cast board_candidate if validation is successful
      board = cast(board_validation.payload, Board)

      #========= Validate the Actor_Candidate =========#
      # Do standard piece validations first
      piece_validation = PieceValidator.validate(actor_candidate)
      if piece_validation.is_failure():
        return ValidationResult(exception=piece_validation.exception)

      # Cast actor_candidate if validation is successful
      piece = cast(piece_validation.payload, Piece)

      # If the piece has no position history its not on the board and cannot piece.
      if piece.current_position is None or piece.positions.is_empty():
        return ValidationResult(exception=ActorNotOnBoardCannotMoveException(
          f"{method}: {ActorNotOnBoardCannotMoveException.DEFAULT_MESSAGE}"
        ))

      # If the piece is not on its team roster it cannot be a TravelEvent actor. This might have been
      # checked by the PieceValidator
      team = piece.team
      if piece not in team.roster:
        return ValidationResult(exception=ActorNotOnRosterCannotMoveException(
          f"{method}: {ActorNotOnRosterCannotMoveException.DEFAULT_MESSAGE}"
        ))

      # A captured combatant cannot be a TravelEvent actor. No need for validating a checkmated
      # king as an actor because the game ends when a king is in checkmate.
      if isinstance(piece, CombatantPiece) and actor_candidate.captor is not None:
        return ValidationResult(exception=CapturedActorCannotMoveException(
          f"{method}: {CapturedActorCannotMoveException.DEFAULT_MESSAGE}"
        ))

      # Check if the piece is on the board. If there is going to be a problem finding the piece on
      # the board an earlier check was likely to fail. If this fails there is probably a data integrity
      # or consistency problem.
      piece_search = BoardPieceSearch.search(
        board=board_candidate,
        search_context=BoardSearchContext(id=actor_candidate.id
      ))
      if piece_search.is_empty():
        return ValidationResult(exception=TravelActorNotFoundException(
            f"{method}: {TravelActorNotFoundException.DEFAULT_MESSAGE}"
        ))

      if piece_search.is_failure():
        return ValidationResult(exception=piece_search.exception)


      #========= Actor's Square Sanity Checks and  =========#
      """
      Ensure Actor_Candidate is on a square. Checking the position history is not enough because a captured piece 
      will still have a position history but it should not be on the board. A thorough check will see if the piece 
      was in the opposing team's hostages. Doing that will introduce more dependencies. Making sure Actor_Candidate 
      is in the square is a good check.
      """

      # Find the square associated with the piece's last position.
      actor_square_search = BoardSquareSearch.search(
        board=board_candidate,
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

      # If the piece is not the square's occupant it cannot be a TravelEvent's actor. Data inconsistency
      # or some other integrity problem is likely.
      if square.occupant is not piece:
        return ValidationResult(exception=SquareMisMatchesTravelActorException(
          f"{method}: {SquareMisMatchesTravelActorException.DEFAULT_MESSAGE}"
        ))

      return ValidationResult(payload=actor_square_search.payload[0])
    except Exception as e:
      return ValidationResult(exception=InvalidTravelActorException(f"{method}: {e}"))