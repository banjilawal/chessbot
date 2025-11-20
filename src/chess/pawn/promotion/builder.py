# src/chess/chess/owner/travel/occupation/factory.py

"""
Module: `chess.owner.travel.occupation.coord_stack_validator`
Author: Banji Lawal
Created: 2025-10-21
version: 1.0.0
"""

from typing import Tuple, cast

from chess.board import Board, BoardSearchContext, BoardSquareSearch
from chess.board.search.context.builder import BoardSearchContextBuilder
from chess.pawn.promotion.event import PromotionEvent
from chess.pawn.promotion.exception import DoublePromotionException
from chess.rank import Bishop, Knight, Pawn, Queen, Rank, Rook
from chess.square import Square
from chess.system import BuildResult, Builder, Event, LoggingLevelRouter, ValidationResult, id_emitter
from chess.piece import (
    PawnPiece, PromotablePiece,
    BoardActorValidator
)


class PromotionEventBuilder(Builder[PromotionEvent]):
    """"""
    PROMOTABLE_RANKS = Tuple[Queen, Knight, Bishop, Rook]
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, actor: Pawn, execution_environment: Board, parent: Event, new_rank: Rank=Queen) -> BuildResult[PromotionEvent]:
        """"""
        method = "PromotionEventBuilder.builder"
        
        try:
            if not isinstance(actor, PawnPiece):
                return BuildResult.failure(TypeError(f"Expected a PawnPiece, got {type(actor).__name__}"))
            
            if not isinstance(new_rank, (Knight, Bishop, Rook, Queen)):
                return BuildResult.failure(TypeError(
                    f"Expected a PromotableRank(knight, bishop, queen ,or rook, got {type(new_rank).__name__}")
                )
            
            actor_validator = BoardActorValidator.validate(actor, execution_environment)
            if actor_validator.is_failure():
                return BuildResult.failure(actor_validator.exception)
            
            actor_candidate, environment_candidate = actor_validator.payload
            
            if not isinstance(actor_candidate, PromotablePiece):
                return BuildResult.failure(
                    TypeError(f"Expected an PromotablePiece, got {type(actor_candidate).__name__}")
                )
            
            actor = cast(PawnPiece, actor_candidate)
            board = cast(Board, environment_candidate)
            
            if actor.current_position.row != actor.team_name.schema.enemy_schema.rank_row:
                return ValidationResult.failure(
                    ActorNotOnPromotionRowException(f"{method}: {ActorNotOnPromotionRowException.DEFAULT_MESSAGE}")
                )
            
            if (
                (actor.previous_rank is not None and not isinstance(actor.rank_name, Queen)) or
                (actor.previous_rank is None and isinstance(actor.rank_name, Queen))
            ):
                return BuildResult.failure(
                    InconsistentRankHistoryException(f"{method}: {InconistenctRankHistoryException.DEFAULT_MESSAGE}")
                )
            
            if piece.previous_rank is not None and isinstance(piece.rank_name, Queen):
                return ValidationResult.failure(
                    DoublePromotionException(f"{method}: {DoublePromotionException.DEFAULT_MESSAGE}")
                )
            
            context_build_result = BoardSearchContextBuilder.build(piece_id=actor.visitor_id)
            if context_build_result.is_failure():
                return ValidationResult.failure(context_build_result.exception)
            context = cast(BoardSearchContext, context_build_result.payload)
            
            square_search_result = BoardSquareSearch.search(board=execution_environment, context=context)
            if square_search_result.is_failure():
                return ValidationResult.failure(square_search_result.exception)
            promotion_square = cast(Square, square_search_result.payload)
            
            return BuildResult.success(
                PromotionEvent(
                    id=id_emitter.event_id,
                    actor=actor,
                    actor_square=promotion_square,
                    new_rank=new_rank,
                    execution_environment=board,
                    parent=parent
                )
            )
        
        except Exception as e:
            return BuildResult.failure(e)