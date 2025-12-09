# src/chess/rank/model/king/exception.py

"""
Module: chess.rank.model.king.exception
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
    #======================# KING EXCEPTION SUPER CLASS #======================#
    "KingException",
    #======================# KING VALIDATION EXCEPTION SUPER CLASS #======================#
    "InvalidKingException",
    "NullKingException",
    #======================# RANK_DESIGNATION #======================#
    "NotKingDesignationException",
    #======================# RANK_ID EXCEPTION #======================#
    "NotKingIdException",
    #======================# RANK_NAME EXCEPTION #======================#
    "NotKingNameException",
    #======================# RANK_QUOTA EXCEPTION #======================#
    "NotKingQuotaException",
    #======================# RANK_RANSOM EXCEPTION #======================#
    "NotKingRansomException",
    #======================# IMPROPER_MOVE EXCEPTION #======================#
    "ImproperKingMoveException",
]


#======================# KING EXCEPTION SUPER CLASS #======================#
class KingException(RankException):
    """
    Catchall for exceptions organic to King properties and its atomic operations."""
    ERROR_CODE = "KING ERROR"
    DEFAULT_MESSAGE = "King raised an exception."


#======================# KING VALIDATION EXCEPTION SUPER CLASS #======================#
class InvalidKingException(KingException, ValidationException):
    """Catchall Exception for KingValidator when a candidate fails a sanity check."""
    ERROR_CODE = "KING_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "King validation failed."


class NullKingException(KingException, ValidationException):
    """Raised if an entity, method, or operation expects a King but gets null instead."""
    ERROR_CODE = "NULL_KING_ERROR"
    DEFAULT_MESSAGE = "King cannot be null."


#======================# RANK_DESIGNATION #======================#
class NotKingDesignationException(KingException, RankDesignationException):
    """Raised when a tested designation is not a King's."""
    ERROR_CODE = "KING_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct King designation."


#======================# RANK_ID EXCEPTION #======================#
class NotKingIdException(KingException, RankIdException):
    """Raised when a tested designation is not a King's."""
    ERROR_CODE = "KING_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct King id."


#======================# RANK_NAME EXCEPTION #======================#
class NotKingNameException(KingException, RankNameException):
    """Raised when a tested name is not a King's."""
    ERROR_CODE = "KING_NAME_ERROR"
    DEFAULT_MESSAGE = "Not the correct King name."


#======================# RANK_QUOTA EXCEPTION #======================#
class NotKingQuotaException(KingException, TeamQuotaException):
    """Raised when a tested quota is not a King's."""
    ERROR_CODE = "KING_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Not the correct King quota for a team."


#======================# RANK_RANSOM EXCEPTION #======================#
class NotKingRansomException(KingException, RankRansomException):
    """Raised when a tested ransom is not a King's."""
    ERROR_CODE = "KING_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Not the correct King ransom."


#======================# IMPROPER_MOVE EXCEPTION #======================#
class ImproperKingMoveException(KingException, ImproperMoveException):
    """Raised when a King's traveling rules prevent it from getting to a position."""
    ERROR_CODE = "IMPROPER_KING_MOVE_ERROR"
    DEFAULT_MESSAGE = "Improper King move."