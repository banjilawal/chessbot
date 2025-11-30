# src/chess/rank/bishop/exception.py

"""
Module: chess.rank.bishop.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import (
    ImproperMoveException, RankDesignationException, RankException, RankIdException, RankNameException,
    RankRansomException, TeamQuotaException
)

__all__ = [
    # ======================# BISHOP EXCEPTION SUPER CLASS #======================#
    "BishopException",
    # ======================# RANK_DESIGNATION #======================#
    "NotBishopDesignationException",
    # ======================# RANK_ID EXCEPTION #======================#
    "NotBishopIdException",
    # ======================# RANK_NAME EXCEPTION #======================#
    "NotBishopNameException",
    # ======================# RANK_QUOTA EXCEPTION #======================#
    "NotBishopQuotaException",
    # ======================# RANK_RANSOM EXCEPTION #======================#
    "NotBishopRansomException",
    # ======================# IMPROPER_MOVE EXCEPTION #======================#
    "ImproperBishopMoveException",
]


# ======================# BISHOP EXCEPTION SUPER CLASS #======================#
class BishopException(RankException):
    """
    Catchall for exceptions organic to Bishop properties and its atomic operations. 
    Use subclass exceptions in debugging
    """
    ERROR_CODE = "BISHOP ERROR"
    DEFAULT_MESSAGE = "Bishop raised an exception."


# ======================# RANK_DESIGNATION #======================#
class NotBishopDesignationException(BishopException, RankDesignationException):
    """Raised when a tested designation is not a Bishop's."""
    ERROR_CODE = "BISHOP_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct Bishop designation."


# ======================# RANK_ID EXCEPTION #======================#
class NotBishopIdException(BishopException, RankIdException):
    """Raised when a tested designation is not a Bishop's."""
    ERROR_CODE = "BISHOP_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Bishop id."


# ======================# RANK_NAME EXCEPTION #======================#
class NotBishopNameException(BishopException, RankNameException):
    """Raised when a tested name is not a Bishop's."""
    ERROR_CODE = "BISHOP_NAME_ERROR"
    DEFAULT_MESSAGE = "Not the correct Bishop name."


# ======================# RANK_QUOTA EXCEPTION #======================#
class NotBishopQuotaException(BishopException, TeamQuotaException):
    """Raised when a tested quota is not a Bishop's."""
    ERROR_CODE = "BISHOP_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Not the correct Bishop quota for a team."


# ======================# RANK_RANSOM EXCEPTION #======================#
class NotBishopRansomException(BishopException, RankRansomException):
    """Raised when a tested ransom is not a Bishop's."""
    ERROR_CODE = "BISHOP_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Not the correct Bishop ransom."


# ======================# IMPROPER_MOVE EXCEPTION #======================#
class ImproperBishopMoveException(BishopException, ImproperMoveException):
    """Raised when a Bishop's traveling rules prevent it from getting to a position."""
    ERROR_CODE = "IMPROPER_BISHOP_MOVE_ERROR"
    DEFAULT_MESSAGE = "Improper Bishop move."