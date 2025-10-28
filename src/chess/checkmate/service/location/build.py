# src/chess/checkmate/post/check/build.py

"""
Module: chess.checkmate.post.check.build
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""
from chess.board import Board
from chess.piece import KingPiece, Piece
from chess.checkmate import KingLocationRecord

from chess.system import BuildResult, Builder, LoggingLevelRouter



class KingLocationRecordBuilder(Builder[KingLocationRecord]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, king: KingPiece, board: Board) -> BuildResult[KingLocationRecord]:
        pass