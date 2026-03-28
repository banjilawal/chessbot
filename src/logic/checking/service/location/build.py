# src/logic/mate/post/check/exception.py

"""
Module: logic.mate.post.check.build
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""
from logic.board import Board
from logic.piece import KingPiece, Piece
from logic.checkmate import KingLocationRecord

from logic.system import BuildResult, BuildTransaction, LoggingLevelRouter



class KingLocationRecordBuildTransaction(BuildTransaction[KingLocationRecord]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, king: KingPiece, board: Board) -> BuildResult[KingLocationRecord]:
        pass