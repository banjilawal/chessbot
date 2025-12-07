# src/chess/rank/spec/exception/ransom/exception.py

"""
Module: chess.rank.spec.exception.ransom.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import RankSpecException
from chess.system import BoundsException, NullException, ValidationException

__all__ = [
    # ======================# RANK_RANSOM EXCEPTION SUPER CLASS #======================#
    "RankRansomException",
    # ======================# NULL RANK_RANSOM EXCEPTIONS #======================#
    "InvalidRankRansomException",
    # ======================# NULL RANK_RANSOM EXCEPTIONS #======================#
    "NullRankRansomException",
    # ======================# RANK_RANSOM BOUNDS EXCEPTIONS #======================#
    "RankRansomBoundsException",
]


# ======================# RANK_RANSOM EXCEPTION SUPER CLASS #======================#
class RankRansomException(RankSpecException):
    """
    Super class of exceptions raised by Rank.ransom objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Rank.ransom raised an exception."


# ======================# RANK_RANSOM VALIDATION EXCEPTION #======================#
class InvalidRankRansomException(RankRansomException, ValidationException):
    """Raised if a RankRansomValidation candidate fails a check."""
    ERROR_CODE = "RANK_RANSOM_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Rank.ransom validation failed."


# ======================# NULL RANK_RANSOM EXCEPTION #======================#
class NullRankRansomException(RankRansomException, NullException):
    """Raised if the Rank.ransom is null."""
    ERROR_CODE = "NULL_RANK_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Rank.ransom cannot be null."


# ======================# RANK_RANSOM BOUNDS EXCEPTIONS #======================#
class RankRansomBoundsException(RankRansomException, BoundsException):
    """Raised if the ransom is not in RankSpec."""
    ERROR_CODE = "RANK_RANSOM_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The ransom is not included in the RankSpec settings."