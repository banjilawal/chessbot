# src/chess/rank/knight/exception.py

"""
Module: chess.rank.knight.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


# ======================# RANK_DESIGNATION #======================#
class NotKnightDesignationException(KnightException, RankDesignationException):
    """Raised when a tested designation is not a Knight's."""
    ERROR_CODE = "KNIGHT_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct Knight designation."


# ======================# RANK_ID EXCEPTIONS #======================#
class NotKnightIdException(KnightException, RankIdException):
    """Raised when a tested designation is not a Pawn's."""
    ERROR_CODE = "PAWN_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn id."


# ======================# RANK_NAME INCONSISTENCY EXCEPTIONS #======================#
class NotKnightNameException(KnightException, RankNameException):
    """Raised when a tested name is not a Knight's."""
    ERROR_CODE = "KNIGHT_NAME_ERROR"
    DEFAULT_MESSAGE = "Not the correct Knight name."


# ======================# RANK_QUOTA INCONSISTENCY EXCEPTIONS #======================#
class NotKnightQuotaException(KnightException, TeamQuotaException):
    """Raised when a tested quota is not a Knight's."""
    ERROR_CODE = "KNIGHT_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Not the correct Knight quota for a team."


# ======================# RANK_RANSOM EXCEPTION #======================#
class NotKnightRansomException(KnightException, RankRansomException):
    """Raised when a tested ransom is not a Knight's."""
    ERROR_CODE = "KNIGHT_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Not the correct Knight ransom."