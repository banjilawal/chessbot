# src/chess/rank/exception.py

"""
Module: chess.rank.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import ChessException, BuildFailedException, NullException

__all__ = [
    #======================# RANK EXCEPTION #======================#
    "RankException",
    #======================# RANK VALIDATION EXCEPTION #======================#
    "NullRankException",
    #======================# RANK BUILD EXCEPTION #======================#
    "RankBuildFailedException",
    #======================# RANK MOVING EXCEPTION #======================#
    "ImproperMoveException",
]


#======================# RANK EXCEPTION #======================#
class RankException(ChessException):
    """
    Super class of exception raised by Rank objects. Do not use directly.
    Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_ERROR"
    DEFAULT_MESSAGE = "Rank raised an exception."

class NullRankException(RankException, NullException):
    ERROR_CODE = "NULL_RANK_ERROR"
    DEFAULT_MESSAGE = "Rank cannot be null."


class RankBuildFailedException(RankException, BuildFailedException):
    """Catchall exception for when RankFactory encounters an error during a Rank build."""
    ERROR_CODE = "RANK_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Rank build failed."


#======================# RANK MOVING EXCEPTION #======================#
class ImproperMoveException(RankException):
    """Raised when a Rank's moving rules prevent a Token from getting to a position."""
    ERROR_CODE = "IMPROPER_MOVE_ERROR"
    DEFAULT_MESSAGE = "Improper move."
