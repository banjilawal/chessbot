# src/chess/piece/travel/validation/destination.py

"""
Module: chess.piece.validation.binding
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.0
"""

from typing import cast, Tuple

from chess.board import Board, BoardPieceSearch, BoardSearchContext, BoardValidator
from chess.piece import Piece, TravelActorValidator, ActorNotOnBoardCannotMoveException
from chess.system import BindingValidator, LoggingLevelRouter, ValidationResult, Validator


class PieceBindingBoardValidator(BindingValidator[Piece, Board]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Tuple[Piece, Board]) -> ValidationResult[Tuple[Piece, Board]]:
        """"""
        method = "PieceBindingBoardValidator.validate"
        
        try:
            piece_candidate, environment_candidate = candidate
            
            travel_actor_validation = TravelActorValidator.validate(piece_candidate)
            if travel_actor_validation.is_failure():
                return ValidationResult.failure(travel_actor_validation.exception)
            
            piece = cast(Piece, travel_actor_validation.payload)
            
            environment_validator = BoardValidator.validate(environment_candidate)
            if environment_validator.is_failure():
                return ValidationResult.failure(environment_validator.exception)
            
            board = cast(Board, environment_validator.payload)
            
            search_result = BoardPieceSearch.search(board=board, search_context=BoardSearchContext(id=piece.id))
            if search_result.is_empty():
                return ValidationResult.failure(
                    ActorNotOnBoardCannotMoveException(f"{method}: {ActorNotOnBoardCannotMoveException.DEFAULT_MESSAGE}")
                )
            
            if search_result.is_failure():
                return ValidationResult.failure(search_result.exception)
            
            return ValidationResult.success(Tuple[piece, board])
        
        except Exception as e:
            return ValidationResult(exception=e)
