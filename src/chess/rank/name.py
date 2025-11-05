# chess/rank/name.py

"""
Module: `chess.rank.name`
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from enum import Enum, auto


class RankName(Enum):
    KING = auto(),
    PAWN = auto(),
    ROOK = auto(),
    QUEEN = auto(),
    BISHOP = auto(),
    KNIGHT = auto(),