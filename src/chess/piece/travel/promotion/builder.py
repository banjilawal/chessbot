# chess/chess/piece/travel/occupation/validator.py

"""
Module: `chess.piece.travel.occupation.validator`
Author: Banji Lawal
Created: 2025-10-21
version: 1.0.0
"""

from typing import Any, cast

from chess.board import Board, BoardSearchContext, BoardSquareSearch
from chess.board.search.context.builder import BoardSearchContextBuilder
from chess.piece.travel.promotion.event import PromotionEvent
from chess.piece.travel.promotion.exception import DoublePromotionException
from chess.rank import Queen
from chess.square import Square
from chess.system import BuildResult, Builder, Event, LoggingLevelRouter, Validator, ValidationResult, id_emitter
from chess.piece import (
    ActorAlreadyAtDestinationException, NullPromotionEventException, OccupationEvent,
    NullOccupationEventException, OccupationDestinationNotEmptyException, PromotablePiece, TravelActorValidator,
    TravelResourceValidator
)


class PromotionEventBuilder(Builder[PromotionEvent]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, actor: PromotablePiece, execution_environment: Board, parent: Event) -> BuildResult[PromotionEvent]:
        """"""
        method = "PromotionEventBuilder.build"
        
        try:
            actor_validator = TravelActorValidator.validate(event.actor, event.execution_environment)
            if actor_validator.is_failure():
                return BuildResult.failure(actor_validator.exception)
            
            actor_candidate, environment_candidate = actor_validator.payload
            
            if not isinstance(actor_candidate, PromotablePiece):
                return BuildResult.failure(
                    TypeError(f"Expected an PromotablePiece, got {type(actor_candidate).__name__}")
                )
            
            actor = cast(PromotablePiece, actor_candidate)
            board = cast(Board, environment_candidate)
            
            if actor.current_position.row != event.actor.team.schema.enemy_schema.rank_row:
                return ValidationResult.failure(
                    ActorNotOnPromotionRowException(f"{method}: {ActorNotOnPromotionRowException.DEFAULT_MESSAGE}")
                )
            
            if (
                (actor.previous_rank is not None and not isinstance(actor.rank, Queen)) or
                (actor.previous_rank is None and isinstance(actor.rank, Queen))
            ):
                return BuildResult.failure(
                    InconsistentRankHistoryException(f"{method}: {InconistenctRankHistoryException.DEFAULT_MESSAGE}")
                )
            
            if piece.previous_rank is not None and isinstance(piece.rank, Queen):
                return ValidationResult.failure(
                    DoublePromotionException(f"{method}: {DoublePromotionException.DEFAULT_MESSAGE}")
                )
            
            context_build_result = BoardSearchContextBuilder.build(piece_id=event.actor.id)
            if context_build_result.is_failure():
                return ValidationResult.failure(context_build_result.exception)
            context = cast(BoardSearchContext, context_build_result.payload)
            
            square_search_result = BoardSquareSearch.search(board=event.execution_environment, context=context)
            if square_search_result.is_failure():
                return ValidationResult.failure(square_search_result.exception)
            promotion_square = cast(Square, square_search_result.payload)
            
            return BuildResult.success(
                PromotionEvent(
                    id=id_emitter.event_id,
                    actor=actor,
                    actor_square=actor_square,
                    execution_environment=board,
                    parent=parent
                )
            )
        
        except Exception as e:
            return BuildResult.failure(e)