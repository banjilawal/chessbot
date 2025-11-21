# src/chess/rank/factory/collision.py

"""
Module: chess.rank.factory.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.rank import RankException
from chess.system import BuildFailedException

__all__ = [
    "RankBuildFailedException",
]




# ======================# RANK BUILD EXCEPTIONS #======================#
class RankBuildFailedException(RankException, BuildFailedException):
    """Catchall Exception for RankFactory when it encounters an error fabricating a Rank."""
    ERROR_CODE = "RANK_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Rank build failed."
