# src/chess/rank/spec/exception/id/exception.py

"""
Module: chess.rank.spec.exception.id.exception
Author: Banji Lawa
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import RankSpecException
from chess.system import BoundsException, NullException, ValidationException

__all__ = [
    # ======================# RANK_ID EXCEPTION SUPER CLASS #======================#
    "RankIdException",
    # ======================# NULL RANK_ID EXCEPTIONS #======================#
    "InvalidRankIdException",
    # ======================# NULL RANK_ID EXCEPTIONS #======================#
    "NullRankIdException",
    # ======================# RANK_ID BOUNDS EXCEPTIONS #======================#
    "RankIdBoundsException",
]


# ======================# RANK_ID EXCEPTION SUPER CLASS #======================#
class RankIdException(RankSpecException):
    """
    Super class of exceptions raised by Rank.id objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_ID_ERROR"
    DEFAULT_MESSAGE = "Rank.id raised an exception."


# ======================# RANK_ID VALIDATION EXCEPTION #======================#
class InvalidRankIdException(RankIdException, ValidationException):
    """Raised if a RankIdValidation candidate fails a check."""
    ERROR_CODE = "RANK_ID_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Rank.id validation failed."


# ======================# NULL RANK_ID EXCEPTION #======================#
class NullRankIdException(RankIdException, NullException):
    """Raised if the Rank.id is null."""
    ERROR_CODE = "NULL_RANK_ID_ERROR"
    DEFAULT_MESSAGE = "Rank.id cannot be null."


# ======================# RANK_ID BOUNDS EXCEPTIONS #======================#
class RankIdBoundsException(RankIdException, BoundsException):
    """Raised if the id is not in RankSpec."""
    ERROR_CODE = "RANK_ID_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "The id is not included in the RankSpec settings."