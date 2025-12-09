# src/chess/rank/spec/exception/exception.py

"""
Module: chess.rank.spec.exception.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import RankException
from chess.system import NullException, ValidationException

__all__ = [
    #======================# RANK_SPEC EXCEPTION SUPER CLASS #======================#
    "RankSpecException",
    
    #======================# RANK_SPEC VALIDATION EXCEPTIONS #======================#
    "InvalidRankSpecException",
    "NullRankSpecException",
]


#======================# RANK_SPEC EXCEPTION SUPER CLASS #======================#
class RankSpecException(RankException):
    """
    Super class of all exceptions RankSpec object raises. Do not use directly. Subclasses give
    details useful for debugging.
    """
    ERROR_CODE = "RANK_SPEC_ERROR"
    DEFAULT_MESSAGE = "RankSpec raised an exception."


#======================# RANK_SPEC VALIDATION EXCEPTIONS #======================#
class InvalidRankSpecException(RankSpecException, ValidationException):
    """
    Raised by RankSpecValidator if an object fails sanity checks. Exists primarily to catch all
    exceptions raised validating an existingRankSpec.
    """
    ERROR_CODE = "RANK_SPEC_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "RankSpec validation failed."


class NullRankSpecException(RankSpecException, NullException):
    """Raised if an entity, method, or operation requires a RankSpec but gets null."""
    ERROR_CODE = "NULL_RANK_SPEC_ERROR"
    DEFAULT_MESSAGE = "RankSpec cannot be null."