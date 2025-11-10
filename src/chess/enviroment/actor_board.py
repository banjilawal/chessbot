# src/chess/environment/actor_board.py

"""
Module: `chess.environment.actor`
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.1
"""

from typing import cast, Tuple

from chess.board import Board, BoardPieceSearch, BoardSearchContext, BoardValidator


from chess.king import KingPiece
from chess.piece import Piece, CombatantPiece
from chess.piece.model.validator import PieceValidator
from chess.system import LoggingLevelRouter, Validator, ValidationResult
from chess.enviroment import (
  NoInitialPlacementException, NullTravelerEnvironmentTupleException, CheckMatedKingCannotMoveException,
  BoardPieceRemovedCannotActException, ActorNotOnRosterCannotMoveException, CapturedActorCannotMoveException
)




"""
Implements the `OccupationExecutor` class, which handles executing travel
directives in the chess engine. This includes moving pieces, capturing enemies,
and coordinating rollback logic in case of inconsistencies or failed operations.

Attributes:
  * `OccupationExecutor:` Main class responsible for executing travel directives.
  * `_attack_enemy`: Static method for processing attacks on enemy pieces.
  * `_run_scan`: Static method for handling discoveries on occupied squares.
  * `_switch_squares`: Static method the transferring team_name owner to team_name different `Square`.
"""
class BoardActorValidator(Validator[Tuple[Piece, Board]]):
  """
  # ROLE: Validator, Data Integrity

  # RESPONSIBILITIES:
  1. Ensure `TravelEvent` actor_candidate has a valid binding to the execution environment for `TravelEventFactory`.
  2. If binding requirements are not satisfied return the appropriate error to `TravelEventFactory` in
      `ValidationResult`.
  3. Discover potential service integrity violations.

  # PROVIDES:
  `ValidationResult`: Return type containing the built `Team` or error information.

  # ATTRIBUTES:
  None
  """

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: Tuple[Piece, Board])-> ValidationResult[Tuple[Piece, Board]]:
    """"""
    method = "BoardActorValidator.validate"

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

      # If the owner has no position history its not on the board and cannot owner.
      if actor.current_position is None or actor.positions.is_empty():
        return ValidationResult.failure(
          NoInitialPlacementException(f"{method}: {NoInitialPlacementException.DEFAULT_MESSAGE}")
        )

      # If the owner is not on its team_name roster it cannot be a TravelEvent actor_candidate. This might have been
      # checked by the PieceValidator
      team = actor.team
      if actor not in team.roster:
        return ValidationResult.failure(
          ActorNotOnRosterCannotMoveException(f"{method}: {ActorNotOnRosterCannotMoveException.DEFAULT_MESSAGE}")
        )

      # A captured combatant cannot be a TravelEvent actor_candidate. No need for validating a checkmated
      # occupation as an actor_candidate because the game ends when a occupation is in checkmate.
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
          BoardPieceRemovedCannotActException(f"{method}: {BoardPieceRemovedCannotActException.DEFAULT_MESSAGE}")
        )
      
      if search_result.is_failure():
        return ValidationResult.failure(search_result.exception)
      
      return ValidationResult.success(Tuple[actor, environment])
    
    except Exception as e:
      return ValidationResult(exception=e)