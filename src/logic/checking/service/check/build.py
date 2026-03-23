# src/logic/mate/post/check/exception.py

"""
Module: logic.mate.post.check.builder
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""

from logic.piece import KingPiece, Piece
from logic.checkmate import CheckRecord

from logic.system import BuildResult, BuildProcess, LoggingLevelRouter



class CheckRecordBuildProcess(BuildProcess[CheckRecord]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, king_checker: Piece, enemy_king: KingPiece) -> BuildResult[CheckRecord]:
        pass