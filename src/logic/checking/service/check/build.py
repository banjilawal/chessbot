# src/logic/mate/post/check/exception.py

"""
Module: logic.mate.post.check.build
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""

from logic.piece import KingPiece, Piece
from logic.checkmate import CheckRecord

from logic.system import BuildResult, BuildTransaction, LoggingLevelRouter



class CheckRecordBuildTransaction(BuildTransaction[CheckRecord]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, king_checker: Piece, enemy_king: KingPiece) -> BuildResult[CheckRecord]:
        pass