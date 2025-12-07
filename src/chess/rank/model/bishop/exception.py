# src/chess/rank/model/bishop/base.py

"""
Module: chess.rank.model.bishop.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ValidationException
from chess.rank import (
    ImproperMoveException, RankDesignationException, RankException, RankIdException, RankNameException,
    RankRansomException, TeamQuotaException
)

__all__ = [
    # ======================# BISHOP EXCEPTION SUPER CLASS #======================#
    "BishopException",
    # ======================# BISHOP VALIDATION EXCEPTION SUPER CLASS #======================#
    "InvalidBishopException",
    "NullBishopException",
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
    Catchall for exceptions organic to Bishop properties and its atomic operations."""
    ERROR_CODE = "BISHOP ERROR"
    DEFAULT_MESSAGE = "Bishop raised an exception."


# ======================# BISHOP VALIDATION EXCEPTION SUPER CLASS #======================#
class InvalidBishopException(BishopException, ValidationException):
    """Catchall Exception for BishopValidator when a candidate fails a sanity check."""
    ERROR_CODE = "BISHOP_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Bishop validation failed."


class NullBishopException(BishopException, ValidationException):
    """Raised if an entity, method, or operation expects a Bishop but gets null instead."""
    ERROR_CODE = "NULL_BISHOP_ERROR"
    DEFAULT_MESSAGE = "Bishop cannot be null."


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