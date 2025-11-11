# src/chess/environment/builder.py

"""
Module: chess.environment.builder
Author: Banji Lawal
Created: 2025-11-10
Version: 1.0.1
"""

from typing import cast


from chess.square import Square
from chess.board import Board, BoardValidator
from chess.piece import Piece, PieceValidator
from chess.enviroment.validator import TurnScene, TurnSceneValidator
from chess.system import Builder, BuildResult, IdValidator, LoggingLevelRouter


class TurnSceneBuilder(Builder[TurnScene]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, id: int, piece: Piece, board: Board) -> BuildResult[TurnScene]:
        """"""
        method = "TurnSceneBuilder.build"
        
        try:
            id_validation = IdValidator.validate(id)
            if id_validation.is_failure():
                return BuildResult.failure(id_validation.exception)
            
            piece_validation = PieceValidator.validate(piece)
            if piece_validation.is_failure():
                return BuildResult.failure(piece_validation.exception)
            
            board_validation = BoardValidator.validate(board)
            if board_validation.is_failure():
                return BuildResult.failure(board_validation.exception)
            
            actor_board_validation = TurnSceneValidator.actor_board_validation_helper(piece=piece, board=board)
            if actor_board_validation.is_failure():
                return BuildResult.failure(actor_board_validation.exception)
            
            actor_square_validation = TurnSceneValidator.actor_square_validation_helper(piece=piece, board=board)
            if actor_square_validation.is_failure():
                return BuildResult.failure(actor_square_validation.exception)
            
            square = cast(Square, actor_square_validation.payload)
            
            return BuildResult.success(
                TurnScene(id=id, actor=piece, board=board, actor_sqaure=square)
            )
            
        except Exception as e:
            return BuildResult.failure(e)