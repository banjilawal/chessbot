# src/chess/piece/travel/validation/actor_candidate.py

"""
Module: chess.piece.travel.validation.actor_candidate
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.0
"""

from typing import cast, Tuple

from chess.board import Board, BoardPieceSearch, BoardSearchContext
from chess.piece import Piece, TravelActorValidator, ActorNotOnBoardCannotMoveException
from chess.system import BindingValidator, LoggingLevelRouter, ValidationResult, Validator


class PieceBindingBoardValidator(BindingValidator[Piece, Board]):
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
  def validate(cls, candidate: Tuple[Piece, Board]) -> ValidationResult[Tuple[Piece, Board]]:
    """"""
    method = "PieceBindingBoardValidator.validate"

    try:
      actor_candidate, environment_candidate = candidate

      travel_actor_validation = TravelActorValidator.validate(actor_candidate)
      if travel_actor_validation.is_failure():
        return ValidationResult(exception=travel_actor_validation.exception)

      piece = cast(Piece, travel_actor_validation.payload)

      exec_environment_validation = Validator.validate(environment_candidate)
      if exec_environment_validation.is_failure():
        return ValidationResult(exception=exec_environment_validation.exception)

      board = cast(Board, exec_environment_validation.payload)

      search_result = BoardPieceSearch.search(board=board, search_context=BoardSearchContext(id=piece.id))
      if search_result.is_empty():
        return ValidationResult(exception=ActorNotOnBoardCannotMoveException(
          f"{method}: {ActorNotOnBoardCannotMoveException.DEFAULT_MESSAGE}"
        ))

      if search_result.is_failure():
        return ValidationResult(exception=search_result.exception)
      #
      #
      #
      #
      # actor_validation = PieceValidator.validate(actor_candidate)
      # if actor_validation.is_failure():
      #   return ValidationResult(exception=actor_validation.exception)
      #
      # piece = cast(Piece, actor_validation.payload)
      #
      # # If the piece has no position history its not on the board and cannot piece.
      # if piece.current_position is None or piece.positions.is_empty():
      #   return ValidationResult(exception=NoInitialPlacementException(
      #     f"{method}: {NoInitialPlacementException.DEFAULT_MESSAGE}"
      #   ))
      #
      # # If the piece is not on its team roster it cannot be a TravelEvent actor_candidate. This might have been
      # # checked by the PieceValidator
      # team = piece.team
      # if piece not in team.roster:
      #   return ValidationResult(exception=ActorNotOnRosterCannotMoveException(
      #     f"{method}: {ActorNotOnRosterCannotMoveException.DEFAULT_MESSAGE}"
      #   ))
      #
      # # A captured combatant cannot be a TravelEvent actor_candidate. No need for validating a checkmated
      # # king as an actor_candidate because the game ends when a king is in checkmate.
      # if isinstance(piece, CombatantPiece) and piece.captor is not None:
      #   return ValidationResult(exception=CapturedActorCannotMoveException(
      #     f"{method}: {CapturedActorCannotMoveException.DEFAULT_MESSAGE}"
      #   ))
      #
      # if isinstance(piece, KingPiece):
      #   enemy_king = cast(KingPiece, piece)
      #   if enemy_king.is_checkmated:
      #     return ValidationResult(exception=CheckMatedKingCannotMoveException(
      #       f"{method}: {CheckMatedKingCannotMoveException.DEFAULT_MESSAGE}"
      #     ))
      #
      # environment_validation = Validator.validate(environment_candidate)
      # if environment_validation.is_failure():
      #   return ValidationResult(exception=environment_validation.exception)
      #
      # board = cast(Board, environment_validation.payload)
      #
      # # Check if the piece is on the board. If there is going to be a problem finding the piece on
      # # the board an earlier check was likely to fail. If this fails there is probably a data integrity
      # # or consistency problem.
      # piece_search = BoardPieceSearch.search(
      #   board=board,
      #   search_context=BoardSearchContext(id=piece.id
      # ))
      # if piece_search.is_empty():
      #   return ValidationResult(exception=TravelActorNotFoundException(
      #       f"{method}: {TravelActorNotFoundException.DEFAULT_MESSAGE}"
      #   ))
      #
      # if piece_search.is_failure():
      #   return ValidationResult(exception=piece_search.exception)
      #
      # # Find the square associated with the piece's last position.
      # square_search = BoardSquareSearch.search(
      #   board=board,
      #   search_context=BoardSearchContext(coord=piece.current_position)
      # )
      #
      # if square_search.is_empty():
      #   return ValidationResult(exception=PieceSquareNotFoundException(
      #     f"{method}: {PieceSquareNotFoundException.DEFAULT_MESSAGE}"
      #   ))
      #
      # if square_search.is_failure():
      #   return ValidationResult(exception=square_search.exception)
      #
      # # Just for safety cast the found square
      # square = cast(Square, square_search.payload[0])
      #
      # # If the piece is not the square's occupant it cannot be a TravelEvent's actor_candidate. Data inconsistency
      # # or some other integrity problem is likely.
      # if square.occupant is not piece:
      #   return ValidationResult(exception=SquareMisMatchesPieceException(
      #     f"{method}: {SquareMisMatchesPieceException.DEFAULT_MESSAGE}"
      #   ))

      return ValidationResult(payload=Tuple[piece, board])
    except Exception as e:
      return ValidationResult(exception=e)