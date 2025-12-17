# src/chess/rank/spec/exception/designation/exception.py

"""
Module: chess.rank.spec.exception.designation.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import RankSpecException
from chess.system import BoundsException, NullException, ValidationException


__all__ = [
    #======================# RANK_NAME EXCEPTION SUPER CLASS #======================#
    "RankNameException",
    #======================# NULL RANK_NAME EXCEPTIONS #======================#
    "InvalidRankNameException",
    #======================# NULL RANK_NAME EXCEPTIONS #======================#
    "NullRankNameException",
    #======================# RANK_NAME BOUNDS EXCEPTIONS #======================#
    "RankNameBoundsException",
]


#======================# RANK_NAME EXCEPTION SUPER CLASS #======================#
class RankNameException(RankSpecException):
    """
    Super class of exceptions raised by Rank.designation objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_NAME_ERROR"
    DEFAULT_MESSAGE = "Rank.designation raised an exception."


#======================# RANK_NAME VALIDATION EXCEPTION #======================#
class InvalidRankNameException(RankNameException, ValidationException):
    """Raised if a RankNameValidation candidate fails a check."""
    ERROR_CODE = "RANK_NAME_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Rank.designation validation failed."


#======================# NULL RANK_NAME EXCEPTION #======================#
class NullRankNameException(RankNameException, NullException):
    """Raised if the Rank.designation is null."""
    ERROR_CODE = "NULL_RANK_NAME_ERROR"
    DEFAULT_MESSAGE = "Rank.designation cannot be null."


#======================# RANK_NAME BOUNDS EXCEPTIONS #======================#
class RankNameBoundsException(RankNameException, BoundsException):
    """Raised if the designation is not in RankSpec."""
    ERROR_CODE = "RANK_NAME_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The designation is not included in the RankSpec settings."