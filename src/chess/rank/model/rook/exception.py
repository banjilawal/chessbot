# src/chess/rank/model/rook/exception.py

"""
Module: chess.rank.model.rook.exception
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
    #======================# ROOK EXCEPTION SUPER CLASS #======================#
    "RookException",
    #======================# ROOK VALIDATION EXCEPTION SUPER CLASS #======================#
    "InvalidRookException",
    "NullRookException",
    #======================# RANK_DESIGNATION #======================#
    "NotRookDesignationException",
    #======================# RANK_ID EXCEPTION #======================#
    "NotRookIdException",
    #======================# RANK_NAME EXCEPTION #======================#
    "NotRookNameException",
    #======================# RANK_QUOTA EXCEPTION #======================#
    "NotRookQuotaException",
    #======================# RANK_RANSOM EXCEPTION #======================#
    "NotRookRansomException",
    #======================# IMPROPER_MOVE EXCEPTION #======================#
    "ImproperRookMoveException",
]


#======================# ROOK EXCEPTION SUPER CLASS #======================#
class RookException(RankException):
    """
    Catchall for exceptions organic to Rook properties and its atomic operations."""
    ERROR_CODE = "ROOK ERROR"
    DEFAULT_MESSAGE = "Rook raised an exception."


#======================# ROOK VALIDATION EXCEPTION SUPER CLASS #======================#
class InvalidRookException(RookException, ValidationException):
    """Catchall Exception for RookValidator when a candidate fails a sanity check."""
    ERROR_CODE = "ROOK_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Rook validation failed."


class NullRookException(RookException, ValidationException):
    """Raised if an entity, method, or operation expects a Rook but gets null instead."""
    ERROR_CODE = "NULL_ROOK_ERROR"
    DEFAULT_MESSAGE = "Rook cannot be null."


#======================# RANK_DESIGNATION #======================#
class NotRookDesignationException(RookException, RankDesignationException):
    """Raised when a tested designation is not a Rook's."""
    ERROR_CODE = "ROOK_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct Rook designation."


#======================# RANK_ID EXCEPTION #======================#
class NotRookIdException(RookException, RankIdException):
    """Raised when a tested designation is not a Rook's."""
    ERROR_CODE = "ROOK_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Rook id."


#======================# RANK_NAME EXCEPTION #======================#
class NotRookNameException(RookException, RankNameException):
    """Raised when a tested designation is not a Rook's."""
    ERROR_CODE = "ROOK_NAME_ERROR"
    DEFAULT_MESSAGE = "Not the correct Rook designation."


#======================# RANK_QUOTA EXCEPTION #======================#
class NotRookQuotaException(RookException, TeamQuotaException):
    """Raised when a tested quota is not a Rook's."""
    ERROR_CODE = "ROOK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Not the correct Rook quota for a team."


#======================# RANK_RANSOM EXCEPTION #======================#
class NotRookRansomException(RookException, RankRansomException):
    """Raised when a tested ransom is not a Rook's."""
    ERROR_CODE = "ROOK_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Not the correct Rook ransom."


#======================# IMPROPER_MOVE EXCEPTION #======================#
class ImproperRookMoveException(RookException, ImproperMoveException):
    """Raised when a Rook's traveling rules prevent it from getting to a position."""
    ERROR_CODE = "IMPROPER_ROOK_MOVE_ERROR"
    DEFAULT_MESSAGE = "Improper Rook move."