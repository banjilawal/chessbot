# src/chess/chess/owner/travel/occupation/factory.py

"""
Module: `chess.owner.travel.occupation.coord_stack_validator`
Author: Banji Lawal
Created: 2025-10-21
version: 1.0.0
"""

from typing import Any, cast

from chess.board import BoardSearchContext, BoardSquareSearch
from chess.board.search.context.builder import BoardSearchContextBuilder
from chess.pawn.promotion.event import PromotionEvent
from chess.pawn.promotion.exception import DoublePromotionException
from chess.rank import Bishop, Knight, Queen, Rook
from chess.square import Square
from chess.system import Validator, ValidationResult
from chess.piece import (
    NullPromotionEventException, OccupationEvent,
    PawnPiece, PromotablePiece,
    BoardActorValidator,
    TravelResourceValidator
)


class OldPromotionEventValidator(Validator[PromotionEvent]):
    """"""
    
    @classmethod
    def validate(cls, candidate: Any) -> ValidationResult[OccupationEvent]:
        """"""
        method = "PromotionEventValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullPromotionEventException(f"{method}: {NullPromotionEventException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance (candidate, PromotionEvent):
                return ValidationResult.failure(
                    TypeError(f"Expected an PromotionEvent, got {type(candidate).__name__} instead.")
                )
            
            event = cast(PromotionEvent, candidate)
            
            id_validation = Validator.validate(candidate.id)
            if not id_validation.is_success():
                return ValidationResult(exception=id_validation.exception)
            
            actor_validator = BoardActorValidator.validate(event.actor, event.execution_environment)
            if actor_validator.is_failure():
                return ValidationResult.failure(actor_validator.exception)
            
            if not isinstance(event.actor, PawnPiece):
                return ValidationResult.failure(
                    TypeError(f"Expected a PawnPiece, got {type(event.actor).__name__}")
                )
            
            if not isinstance(event.new_rank, (Knight, Bishop, Rook, Queen)):
                return ValidationResult.failure(
                    TypeError(
                        f"Expected a PromotableRank(knight, bishop, queen ,or rook, got {type(event.new_rank).__name__}")
                )
                
            
            if event.actor.current_position.row != event.actor.team_name.schema.enemy_schema.rank_row:
                return ValidationResult.failure(
                    ActorNotOnPromotionRowException(f"{method}: {ActorNotOnPromotionRowException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(event.actor, PromotablePiece):
                return ValidationResult.failure(
                    TypeError(f"Expected an PromotablePiece, got {type(candidate).__name__} instead.")
                )
            piece = cast(PromotablePiece, event.actor)
            
            if (
                (piece.previous_rank is not None and not isinstance(piece.rank_name, Queen)) or
                (piece.previous_rank is None and isinstance(piece.rank_name, Queen))
            ):
                return ValidationResult.failure(
                    InconsistentRankHistoryException(f"{method}: {InconistenctRankHistoryException.DEFAULT_MESSAGE}")
                )
            
            if piece.previous_rank is not None and isinstance(piece.rank_name, Queen):
                return ValidationResult.failure(
                    DoublePromotionException(f"{method}: {DoublePromotionException.DEFAULT_MESSAGE}")
                )
            
            context_build_result = BoardSearchContextBuilder.build(piece_id=event.actor.visitor_id)
            if context_build_result.is_failure():
                return ValidationResult.failure(context_build_result.exception)
            context = cast(BoardSearchContext, context_build_result.payload)
            
            square_search_result = BoardSquareSearch.search(board=event.execution_environment, context=context)
            if square_search_result.is_failure():
                return ValidationResult.failure(square_search_result.exception)
            square = cast(Square, square_search_result.payload)
            
            resource_validation = TravelResourceValidator.validate(event.square, event.execution_environment)
            if resource_validation.is_failure():
                return ValidationResult(exception=resource_validation.exception)
            
            
            return ValidationResult(payload=event)
        
        except Exception as e:
            return ValidationResult(exception=e)