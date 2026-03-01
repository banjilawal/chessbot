# src/logic/checkmate/post/check/builder.py

"""
Module: logic.checkmate.post.check.builder
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""
from logic.board import Board
from logic.piece import KingPiece, Piece
from logic.checkmate import KingLocationRecord

from logic.system import BuildResult, Builder, LoggingLevelRouter



class KingLocationRecordBuilder(Builder[KingLocationRecord]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, king: KingPiece, board: Board) -> BuildResult[KingLocationRecord]:
        pass