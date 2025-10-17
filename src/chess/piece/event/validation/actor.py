# src/chess/piece/event/transaction.py

"""
Module: chess.piece.event.transaction
Author: Banji Lawal
Created: 2025-09-28
"""

from chess.square import Square
from chess.system import LoggingLevelRouter, ValidationResult, ActorValidator
from chess.board import Board, BoardPieceSearch, BoardSquareSearch, BoardSearchContext

from chess.piece import (
  Piece, CombatantPiece, PieceValidator, InvalidTravelActorException, ActorNotOnRosterCannotMoveException,
  ActorNotOnBoardCannotMoveException, CapturedActorCannotMoveException,  TravelActorNotFoundException,
  TravelActorSquareNotFoundException
)

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
  """"""

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, actor: Piece, board: Board) -> ValidationResult[Square]:
    """"""
    method = "TravelActorValidator.validate"

    try:
      #========= Actor Sanity Checks =========#
      piece_validation = PieceValidator.validate(actor)
      if piece_validation.is_failure():
        return ValidationResult(exception=piece_validation.exception)

      piece_search = BoardPieceSearch.search(board=board, search_context=BoardSearchContext(id=actor.id))
      if piece_search.is_empty():
        return ValidationResult(exception=TravelActorNotFoundException(
            f"{method}: {TravelActorNotFoundException.DEFAULT_MESSAGE}"
        ))

      if piece_search.is_failure():
        return ValidationResult(exception=piece_search.exception)

      team = actor.team
      if actor not in team.roster:
        return ValidationResult(exception=ActorNotOnRosterCannotMoveException(
          f"{method}: {ActorNotOnRosterCannotMoveException.DEFAULT_MESSAGE}"
        ))

      if actor.current_position is None or actor.positions.is_empty():
        return ValidationResult(exception=ActorNotOnBoardCannotMoveException(
          f"{method}: {ActorNotOnBoardCannotMoveException.DEFAULT_MESSAGE}"
        ))

      if isinstance(actor, CombatantPiece) and actor.captor is not None:
        return ValidationResult(exception=CapturedActorCannotMoveException(
          f"{method}: {CapturedActorCannotMoveException.DEFAULT_MESSAGE}"
        ))

      #========= Actor's Square Sanity Checks and  =========#
      actor_square_search = BoardSquareSearch.search(
        board=board,
        search_context=BoardSearchContext(coord=actor.current_position)
      )

      if actor_square_search.is_empty():
        return ValidationResult(exception=TravelActorSquareNotFoundException(
          f"{method}: {TravelActorSquareNotFoundException.DEFAULT_MESSAGE}"
        ))

      if actor_square_search.is_failure():
        return ValidationResult(exception=actor_square_search.exception)

      return ValidationResult(payload=actor_square_search.payload[0])
    except Exception as e:
      return ValidationResult(exception=InvalidTravelActorException(f"{method}: {e}"))



    # """
    # # ACTION:
    # Verify the `candidate` is a valid ID. The Application requires
    # 1. Candidate is not null.
    # 2. Is a positive integer.
    #
    # # PARAMETERS:
    #     * `candidate` (`int`): the id.
    #
    # # RETURNS:
    # `ValidationResult[str]`: A `ValidationResult` containing either:
    #     `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
    #     `exception` (`Exception`) - An exception detailing which naming rule was broken.
    #
    # # RAISES:
    # `InvalidTravelActorException`: Wraps any specification violations including:
    #     * `TypeError`: if candidate is not an `int`
    #     * `IdNullException`: if candidate is null
    #     * `NegativeIdException`: if candidate is negative `
    # """