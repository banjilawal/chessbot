# src/chess/rank/queen/exception.py

"""
Module: chess.rank.queen.exception
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
    # ======================# QUEEN EXCEPTION SUPER CLASS #======================#
    "QueenException",
    # ======================# QUEEN VALIDATION EXCEPTION SUPER CLASS #======================#
    "InvalidQueenException",
    "NullQueenException",
    # ======================# RANK_DESIGNATION #======================#
    "NotQueenDesignationException",
    # ======================# RANK_ID EXCEPTION #======================#
    "NotQueenIdException",
    # ======================# RANK_NAME EXCEPTION #======================#
    "NotQueenNameException",
    # ======================# RANK_QUOTA EXCEPTION #======================#
    "NotQueenQuotaException",
    # ======================# RANK_RANSOM EXCEPTION #======================#
    "NotQueenRansomException",
    # ======================# IMPROPER_MOVE EXCEPTION #======================#
    "ImproperQueenMoveException",
]


# ======================# QUEEN EXCEPTION SUPER CLASS #======================#
class QueenException(RankException):
    """
    Catchall for exceptions organic to Queen properties and its atomic operations."""
    ERROR_CODE = "QUEEN ERROR"
    DEFAULT_MESSAGE = "Queen raised an exception."


# ======================# QUEEN VALIDATION EXCEPTION SUPER CLASS #======================#
class InvalidQueenException(QueenException, ValidationException):
    """Catchall Exception for QueenValidator when a candidate fails a sanity check."""
    ERROR_CODE = "QUEEN_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Queen validation failed."


class NullQueenException(QueenException, ValidationException):
    """Raised if an entity, method, or operation expects a Queen but gets null instead."""
    ERROR_CODE = "NULL_QUEEN_ERROR"
    DEFAULT_MESSAGE = "Queen cannot be null."


# ======================# RANK_DESIGNATION #======================#
class NotQueenDesignationException(QueenException, RankDesignationException):
    """Raised when a tested designation is not a Queen's."""
    ERROR_CODE = "QUEEN_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct Queen designation."


# ======================# RANK_ID EXCEPTION #======================#
class NotQueenIdException(QueenException, RankIdException):
    """Raised when a tested designation is not a Queen's."""
    ERROR_CODE = "QUEEN_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Queen id."


# ======================# RANK_NAME EXCEPTION #======================#
class NotQueenNameException(QueenException, RankNameException):
    """Raised when a tested name is not a Queen's."""
    ERROR_CODE = "QUEEN_NAME_ERROR"
    DEFAULT_MESSAGE = "Not the correct Queen name."


# ======================# RANK_QUOTA EXCEPTION #======================#
class NotQueenQuotaException(QueenException, TeamQuotaException):
    """Raised when a tested quota is not a Queen's."""
    ERROR_CODE = "QUEEN_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Not the correct Queen quota for a team."


# ======================# RANK_RANSOM EXCEPTION #======================#
class NotQueenRansomException(QueenException, RankRansomException):
    """Raised when a tested ransom is not a Queen's."""
    ERROR_CODE = "QUEEN_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Not the correct Queen ransom."


# ======================# IMPROPER_MOVE EXCEPTION #======================#
class ImproperQueenMoveException(QueenException, ImproperMoveException):
    """Raised when a Queen's traveling rules prevent it from getting to a position."""
    ERROR_CODE = "IMPROPER_QUEEN_MOVE_ERROR"
    DEFAULT_MESSAGE = "Improper Queen move."