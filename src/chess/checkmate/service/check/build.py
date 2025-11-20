# src/chess/checkmate/post/check/builder.py

"""
Module: chess.checkmate.post.check.builder
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""

from chess.piece import KingPiece, Piece
from chess.checkmate import CheckRecord

from chess.system import BuildResult, Builder, LoggingLevelRouter



class CheckRecordBuilder(Builder[CheckRecord]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, king_checker: Piece, enemy_king: KingPiece) -> BuildResult[CheckRecord]:
        pass