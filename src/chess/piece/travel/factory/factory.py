# src/chess/piece/travel/factory/factory.py

"""
Module: chess.piece.travel.factory.factory
Author: Banji Lawal
Created: 2025-10-21
version: 1.0.0
"""

from typing import cast

from chess.rank import Queen
from chess.square import Square
from chess.system import LoggingLevelRouter, BuildResult, id_emitter
from chess.board import Board, BoardSquareSearch, BoardSearchContext, CoordSearchInvariantBreachException
from chess.piece import (
    KingCheckEvent, Piece, KingPiece, CombatantPiece, AttackEvent, OccupationEvent, BlockingEvent, PromotablePiece,
    PromotionEvent, BoardActorValidator, TravelEvent, TravelResourceValidator, ActorAlreadyAtDestinationException
)


class TravelEventFactory:
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
    
    @staticmethod
    @LoggingLevelRouter.monitor
    def create(actor: Piece, destination_square: Square, board: Board) -> BuildResult[TravelEvent]:
        """
        # ACTION:
        Verify the `candidate` is a valid ID. The Application requires
        1. Candidate is not null.
        2. Is a positive integer.
    
        # PARAMETERS:
            * `candidate` (`int`): the id.
    
        # RETURNS:
        `ValidationResult[str]`: A `ValidationResult` containing either:
            `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
            `rollback_exception` (`Exception`) - An rollback_exception detailing which naming rule was broken.
    
        # RAISES:
        `InvalidIdException`: Wraps any specification violations including:
            * `TypeError`: if candidate is not an `int`
            * `IdNullException`: if candidate is null
            * `NegativeIdException`: if candidate is negative `
        """
        method = "TravelEventFactory.execute"
        
        try:
            actor_validation = BoardActorValidator.validate((actor, board))
            if actor_validation.is_failure():
                return BuildResult.failure(actor_validation.exception)
            
            resource_validator = TravelResourceValidator.validate((destination_square, board))
            if resource_validator.is_failure():
                return BuildResult.failure(resource_validator.exception)
            
            if actor.current_position == destination_square.coord:
                return BuildResult.failure(
                    ActorAlreadyAtDestinationException(
                        f"{method}: {ActorAlreadyAtDestinationException.DEFAULT_MESSAGE}"
                        )
                )
            
            actor_square_search = BoardSquareSearch.search(
                board=board,
                search_context=BoardSearchContext(coord=actor.current_position)
            )
            
            if actor_square_search.is_empty():
                return BuildResult.failure(
                    CoordSearchInvariantBreachException(
                        f"{method}: {CoordSearchInvariantBreachException.DEFAULT_MESSAGE}"
                    )
                )
            
            if actor_square_search.is_failure():
                return BuildResult.failure(actor_square_search.exception)
            
            actor_square = actor_square_search.payload[0]
            destination_occupant = destination_square.occupant
            
            if destination_occupant is None:
                return TravelEventFactory._process_empty_square(actor, actor_square, destination_square, board)
            
            return TravelEventFactory._process_occupied_square(
                actor, actor_square, destination_occupant, destination_square, board
            )
        
        except Exception as e:
            return BuildResult(exception=e)
    
    @staticmethod
    @LoggingLevelRouter.monitor
    def _process_empty_square(
            actor: Piece, actor_square: Square, empty_square: Square, board: Board
    ) -> BuildResult[TravelEvent]:
        if isinstance(actor, PromotablePiece) and (
                not isinstance(actor.rank, Queen) and
                cast(PromotablePiece, actor).previous_rank is None and
                actor.current_position.row == actor.team.schema.enemy_schema.rank_row and
                actor.current_position.row == empty_square.coord.row
        ):
            return BuildResult.success(
                PromotionEvent(
                    actor=actor,
                    id=id_emitter.event_id,
                    actor_square=actor_square,
                    promotion_square=empty_square,
                    execution_environment=board
                )
            )
        
        return BuildResult.success(
            OccupationEvent(
                actor=actor,
                id=id_emitter.event_id,
                actor_square=actor_square,
                destination_square=empty_square,
                execution_environment=board
            )
        )
    
    @staticmethod
    @LoggingLevelRouter.monitor
    def _process_occupied_square(
            actor: Piece, actor_square: Square, destination_occupant: Piece, destination_square: Square, board: Board
    ) -> BuildResult[TravelEvent]:
        if not actor.is_enemy(destination_occupant):
            return BuildResult.success(
                BlockingEvent(
                    actor=actor,
                    id=id_emitter.event_id,
                    friend=destination_occupant,
                    blocked_square=destination_square,
                    execution_environment=board
                )
            )
        
        if actor.is_enemy(destination_occupant) and isinstance(destination_occupant, KingPiece):
            return BuildResult.success(
                KingCheckEvent(
                    actor=actor,
                    id=id_emitter.event_id,
                    enemy_king=destination_occupant,
                    enemy_square=destination_square,
                    execution_environment=board
                )
            )
        
        return BuildResult.success(
            AttackEvent(
                actor=actor,
                id=id_emitter.event_id,
                actor_square=actor_square,
                enemy_square=destination_square,
                enemy_combatant=cast(CombatantPiece, destination_occupant),
                execution_environment=board
            )
        )
