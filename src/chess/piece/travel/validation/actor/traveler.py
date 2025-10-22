# src/chess/piece/travel/validation/actor_candidate.py

"""
Module: chess.piece.travel.validation.actor_candidate
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.0

"""
from typing import TypeVar, cast, Tuple

from chess.piece.event.validation.actor.exception import CheckMatedKingCannotMoveException, NoInitialPlacementException
from chess.piece.model.piece import CombatantPiece, KingPiece
from chess.piece.travel.validation.actor.exception import NullTravelerEnvironmentTupleException
from chess.square import Square
from chess.system import BindingValidator, LoggingLevelRouter, ValidationResult, Validator
from chess.board import Board, BoardPieceSearch, BoardSquareSearch, BoardSearchContext, BoardValidator

from chess.piece import (
  ActorNotOnRosterCannotMoveException, CapturedActorCannotMoveException, Piece, InvalidTravelActorException,
  ActorNotOnBoardCannotMoveException,
  PieceValidator, TravelActorNotFoundException,
  TravelActorSquareNotFoundException, SquareMisMatchesTravelActorException
)

T = TypeVar('T')

"""
Implements the `OccupationExecutor` class, which handles executing travel
directives in the chess engine. This includes moving pieces, capturing enemies,
and coordinating rollback logic in case of inconsistencies or failed operations.

Attributes:
  * `OccupationExecutor:` Main class responsible for executing travel directives.
  * `_attack_enemy`: Static method for processing attacks on enemy pieces.
  * `_run_scan`: Static method for handling discoveries on occupied squares.
  * `_switch_squares`: Static method the transferring team piece to team different `Square`.
"""
class TravelActorValidator(Validator[Tuple[Piece, Board]]):
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
  def validate(cls, candidate: Tuple[Piece, Board])-> ValidationResult[Tuple[Piece, Board]]:
    """"""
    method = "TravelActorValidator.validate"

    try:
      if candidate is None:
        return ValidationResult.failure(
          NullTravelerEnvironmentTupleException(f"{method}: {NullTravelerEnvironmentTupleException.DEFAULT_MESSAGE}")
        )
      
      actor_candidate, environment_candidate = candidate
      
      actor_validation = PieceValidator.validate(actor_candidate)
      if actor_validation.is_failure():
        return ValidationResult.failure(actor_validation.exception)

      actor = cast(Piece, actor_validation.payload)

      # If the piece has no position history its not on the board and cannot piece.
      if actor.current_position is None or actor.positions.is_empty():
        return ValidationResult.failure(
          NoInitialPlacementException(f"{method}: {NoInitialPlacementException.DEFAULT_MESSAGE}")
        )

      # If the piece is not on its team roster it cannot be a TravelEvent actor_candidate. This might have been
      # checked by the PieceValidator
      team = actor.team
      if actor not in team.roster:
        return ValidationResult.failure(
          ActorNotOnRosterCannotMoveException(f"{method}: {ActorNotOnRosterCannotMoveException.DEFAULT_MESSAGE}")
        )

      # A captured combatant cannot be a TravelEvent actor_candidate. No need for validating a checkmated
      # king as an actor_candidate because the game ends when a king is in checkmate.
      if isinstance(actor, CombatantPiece) and cast(CombatantPiece, actor).captor is not None:
        return ValidationResult.failure(
          CapturedActorCannotMoveException(f"{method}: {CapturedActorCannotMoveException.DEFAULT_MESSAGE}")
        )

      if isinstance(actor, KingPiece) and cast(KingPiece, actor).is_checkmated:
          return ValidationResult.failure(
            CheckMatedKingCannotMoveException(f"{method}: {CheckMatedKingCannotMoveException.DEFAULT_MESSAGE}")
          )
      
      environment_validation = BoardValidator.validate(environment_candidate)
      if environment_validation.is_failure():
        return ValidationResult.failure(environment_validation.exception)
      
      environment = cast(Board, environment_validation.payload)
      
      search_result = BoardPieceSearch.search(board=environment, search_context=BoardSearchContext(id=actor.id))
      if search_result.is_empty():
        return ValidationResult.failure(
          ActorNotOnBoardCannotMoveException(f"{method}: {ActorNotOnBoardCannotMoveException.DEFAULT_MESSAGE}")
        )
      
      if search_result.is_failure():
        return ValidationResult.failure(search_result.exception)
      
      return ValidationResult(payload=Tuple[actor, environment])
    
    except Exception as e:
      return ValidationResult(exception=e)