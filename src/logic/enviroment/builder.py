# src/logic/environment/exception.py

"""
Module: logic.environment.build
Author: Banji Lawal
Created: 2025-11-10
Version: 1.0.1
"""

from typing import cast


from logic.square import Square
from logic.board import Board, BoardValidationProcess
from logic.piece import Piece, PieceValidator
from logic.enviroment.validator import TurnScene, TurnSceneValidationProcess
from logic.system import BuildProcess, BuildResult, IdValidationProcess, LoggingLevelRouter


class TurnSceneBuildProcess(BuildProcess[TurnScene]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, id: int, piece: Piece, board: Board) -> BuildResult[TurnScene]:
        """"""
        method = "TurnSceneBuildProcess.build"
        
        try:
            id_validation = IdValidationProcess.execute(id)
            if id_validation.is_failure():
                return BuildResult.failure(id_validation.exception)
            
            piece_validation = PieceValidator.validate_piece_is_actionable(piece)
            if piece_validation.is_failure():
                return BuildResult.failure(piece_validation.exception)
            
            board_validation = BoardValidationProcess.execute(board)
            if board_validation.is_failure():
                return BuildResult.failure(board_validation.exception)
            
            actor_board_validation = TurnSceneValidationProcess.actor_board_validation_helper(piece=piece, board=board)
            if actor_board_validation.is_failure():
                return BuildResult.failure(actor_board_validation.exception)
            
            actor_square_validation = TurnSceneValidationProcess.actor_square_validation_helper(piece=piece, board=board)
            if actor_square_validation.is_failure():
                return BuildResult.failure(actor_square_validation.exception)
            
            square = cast(Square, actor_square_validation.payload)
            
            return BuildResult.success(
                TurnScene(id=id, actor=piece, board=board, actor_sqaure=square)
            )
            
        except Exception as e:
            return BuildResult.failure(e)