# src/chess/rank/spec/exception/name/exception.py

"""
Module: chess.rank.spec.exception.name.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import RankSpecException
from chess.system import BoundsException, NullException, ValidationException


__all__ = [
    # ======================# RANK_NAME EXCEPTION SUPER CLASS #======================#
    "RankNameException",
    # ======================# NULL RANK_NAME EXCEPTIONS #======================#
    "InvalidRankNameException",
    # ======================# NULL RANK_NAME EXCEPTIONS #======================#
    "NullRankNameException",
    # ======================# RANK_NAME BOUNDS EXCEPTIONS #======================#
    "RankNameBoundsException",
]


# ======================# RANK_NAME EXCEPTION SUPER CLASS #======================#
class RankNameException(RankSpecException):
    """
    Super class of exceptions raised by Rank.name objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_NAME_ERROR"
    DEFAULT_MESSAGE = "Rank.name raised an exception."


# ======================# RANK_NAME VALIDATION EXCEPTION #======================#
class InvalidRankNameException(RankNameException, ValidationException):
    """Raised if a RankNameValidation candidate fails a check."""
    ERROR_CODE = "RANK_NAME_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Rank.name validation failed."


# ======================# NULL RANK_NAME EXCEPTION #======================#
class NullRankNameException(RankNameException, NullException):
    """Raised if the Rank.name is null."""
    ERROR_CODE = "NULL_RANK_NAME_ERROR"
    DEFAULT_MESSAGE = "Rank.name cannot be null."


# ======================# RANK_NAME BOUNDS EXCEPTIONS #======================#
class RankNameBoundsException(RankNameException, BoundsException):
    """Raised if the name is not in RankSpec."""
    ERROR_CODE = "RANK_NAME_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Name is not allowed by RankSpec settings."