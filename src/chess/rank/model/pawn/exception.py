# src/chess/rank/model/pawn/base.py

"""
Module: chess.rank.model.pawn.exception
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
    # ======================# PAWN EXCEPTION SUPER CLASS #======================#
    "PawnException",
    # ======================# PAWN VALIDATION EXCEPTION SUPER CLASS #======================#
    "InvalidPawnException",
    "NullPawnException",
    # ======================# RANK_DESIGNATION #======================#
    "NotPawnDesignationException",
    # ======================# RANK_ID EXCEPTION #======================#
    "NotPawnIdException",
    # ======================# RANK_NAME EXCEPTION #======================#
    "NotPawnNameException",
    # ======================# RANK_QUOTA EXCEPTION #======================#
    "NotPawnQuotaException",
    # ======================# RANK_RANSOM EXCEPTION #======================#
    "NotPawnRansomException",
    # ======================# IMPROPER_MOVE EXCEPTION #======================#
    "ImproperPawnMoveException",
]


# ======================# PAWN EXCEPTION SUPER CLASS #======================#
class PawnException(RankException):
    """
    Catchall for exceptions organic to Pawn properties and its atomic operations."""
    ERROR_CODE = "PAWN ERROR"
    DEFAULT_MESSAGE = "Pawn raised an exception."


# ======================# PAWN VALIDATION EXCEPTION SUPER CLASS #======================#
class InvalidPawnException(PawnException, ValidationException):
    """Catchall Exception for PawnValidator when a candidate fails a sanity check."""
    ERROR_CODE = "PAWN_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Pawn validation failed."


class NullPawnException(PawnException, ValidationException):
    """Raised if an entity, method, or operation expects a Pawn but gets null instead."""
    ERROR_CODE = "NULL_PAWN_ERROR"
    DEFAULT_MESSAGE = "Pawn cannot be null."


# ======================# RANK_DESIGNATION #======================#
class NotPawnDesignationException(PawnException, RankDesignationException):
    """Raised when a tested designation is not a Pawn's."""
    ERROR_CODE = "PAWN_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn designation."


# ======================# RANK_ID EXCEPTION #======================#
class NotPawnIdException(PawnException, RankIdException):
    """Raised when a tested designation is not a Pawn's."""
    ERROR_CODE = "PAWN_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn id."


# ======================# RANK_NAME EXCEPTION #======================#
class NotPawnNameException(PawnException, RankNameException):
    """Raised when a tested name is not a Pawn's."""
    ERROR_CODE = "PAWN_NAME_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn name."


# ======================# RANK_QUOTA EXCEPTION #======================#
class NotPawnQuotaException(PawnException, TeamQuotaException):
    """Raised when a tested quota is not a Pawn's."""
    ERROR_CODE = "PAWN_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn quota for a team."


# ======================# RANK_RANSOM EXCEPTION #======================#
class NotPawnRansomException(PawnException, RankRansomException):
    """Raised when a tested ransom is not a Pawn's."""
    ERROR_CODE = "PAWN_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn ransom."


# ======================# IMPROPER_MOVE EXCEPTION #======================#
class ImproperPawnMoveException(PawnException, ImproperMoveException):
    """Raised when a Pawn's traveling rules prevent it from getting to a position."""
    ERROR_CODE = "IMPROPER_PAWN_MOVE_ERROR"
    DEFAULT_MESSAGE = "Improper Pawn move."