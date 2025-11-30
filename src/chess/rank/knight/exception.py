# src/chess/rank/knight/exception.py

"""
Module: chess.rank.knight.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import (
    ImproperMoveException, RankDesignationException, RankException, RankIdException, RankNameException,
    RankRansomException, TeamQuotaException
)

__all__ = [
    # ======================# KNIGHT EXCEPTION SUPER CLASS #======================#
    "KnightException",
    # ======================# RANK_DESIGNATION #======================#
    "NotKnightDesignationException",
    # ======================# RANK_ID EXCEPTION #======================#
    "NotKnightIdException",
    # ======================# RANK_NAME EXCEPTION #======================#
    "NotKnightNameException",
    # ======================# RANK_QUOTA EXCEPTION #======================#
    "NotKnightQuotaException",
    # ======================# RANK_RANSOM EXCEPTION #======================#
    "NotKnightRansomException",
    # ======================# IMPROPER_MOVE EXCEPTION #======================#
    "ImproperKnightMoveException",
]


# ======================# KNIGHT EXCEPTION SUPER CLASS #======================#
class KnightException(RankException):
    """
    Catchall for exceptions organic to Knight properties and its atomic operations. 
    Use subclass exceptions in debugging
    """
    ERROR_CODE = "KNIGHT ERROR"
    DEFAULT_MESSAGE = "Knight raised an exception."


# ======================# RANK_DESIGNATION #======================#
class NotKnightDesignationException(KnightException, RankDesignationException):
    """Raised when a tested designation is not a Knight's."""
    ERROR_CODE = "KNIGHT_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct Knight designation."


# ======================# RANK_ID EXCEPTION #======================#
class NotKnightIdException(KnightException, RankIdException):
    """Raised when a tested designation is not a Knight's."""
    ERROR_CODE = "KNIGHT_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Knight id."


# ======================# RANK_NAME EXCEPTION #======================#
class NotKnightNameException(KnightException, RankNameException):
    """Raised when a tested name is not a Knight's."""
    ERROR_CODE = "KNIGHT_NAME_ERROR"
    DEFAULT_MESSAGE = "Not the correct Knight name."


# ======================# RANK_QUOTA EXCEPTION #======================#
class NotKnightQuotaException(KnightException, TeamQuotaException):
    """Raised when a tested quota is not a Knight's."""
    ERROR_CODE = "KNIGHT_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Not the correct Knight quota for a team."


# ======================# RANK_RANSOM EXCEPTION #======================#
class NotKnightRansomException(KnightException, RankRansomException):
    """Raised when a tested ransom is not a Knight's."""
    ERROR_CODE = "KNIGHT_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Not the correct Knight ransom."


# ======================# IMPROPER_MOVE EXCEPTION #======================#
class ImproperKnightMoveException(KnightException, ImproperMoveException):
    """Raised when a Knight's traveling rules prevent it from getting to a position."""
    ERROR_CODE = "IMPROPER_KNIGHT_MOVE_ERROR"
    DEFAULT_MESSAGE = "Improper Knight move."