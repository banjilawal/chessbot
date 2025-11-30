# src/chess/rank/validator/ransom/collision.py

"""
Module: chess.rank.validator.ransom.exception
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from chess.system import NullException
from chess.rank import RankException


__all__ = [
  "RankRansomException",

# ======================# NULL RANK_RANSOM EXCEPTIONS #======================#
  "NullRankRansomException",
  
# ======================# RANK_RANSOM BOUNDS EXCEPTIONS #======================#
  "RankRansomBelowBoundsException",
  "RankRansomAboveBoundsException",
  
# ======================# RANK_RANSOM INCONSISTENCY EXCEPTIONS #======================#
  "KingRansomException",
  "QueenRansomException",
  "BishopRansomException",
  "RookRansomException",
  "KnightRansomException",
  "PawnRansomException",
]

