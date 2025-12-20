# src/chess/rank/factory/exception.py

"""
Module: chess.rank.factory.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.rank import RankException
from chess.system import BuildFailedException

__all__ = [
    #======================# RANK BUILD EXCEPTION #======================#
    "RankBuildFailedException",
]


#======================# RANK BUILD EXCEPTION #======================#
class RankBuildFailedException(RankException, BuildFailedException):
    """
    Catchall/wrapper exception for when a condition not handled directly by RankBuilder 
    prevents successful Rank creation.
    """
    ERROR_CODE = "RANK_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Rank build failed."
