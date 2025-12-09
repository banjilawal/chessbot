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
#======================# RANK_DESIGNATION EXCEPTION SUPER CLASS #======================#
    "RankDesignationException",
#======================# NULL RANK_DESIGNATION EXCEPTIONS #======================#
    "InvalidRankDesignationException",
#======================# NULL RANK_DESIGNATION EXCEPTIONS #======================#
    "NullRankDesignationException",
#======================# RANK_DESIGNATION BOUNDS EXCEPTIONS #======================#
    "RankDesignationBoundsException",
]

#======================# RANK_DESIGNATION EXCEPTION SUPER CLASS #======================#
class RankDesignationException(RankSpecException):
    """
    Super class of exceptions raised by Rank.designation objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Rank.designation raised an exception."


#======================# RANK_DESIGNATION VALIDATION EXCEPTION #======================#
class InvalidRankDesignationException(RankDesignationException, ValidationException):
    """Raised if a RankDesignationValidation candidate fails a check."""
    ERROR_CODE = "RANK_DESIGNATION_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Rank.designation validation failed."


#======================# NULL RANK_DESIGNATION EXCEPTION #======================#
class NullRankDesignationException(RankDesignationException, NullException):
    """Raised if the Rank.designation is null."""
    ERROR_CODE = "NULL_RANK_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Rank.designation cannot be null."


#======================# RANK_DESIGNATION BOUNDS EXCEPTIONS #======================#
class RankDesignationBoundsException(RankDesignationException, BoundsException):
    """Raised if the designation is not in RankSpec."""
    ERROR_CODE = "RANK_DESIGNATION_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The designation is not included in the RankSpec settings."