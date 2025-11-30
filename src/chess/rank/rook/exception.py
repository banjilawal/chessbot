# src/chess/rank/rook/exception.py

"""
Module: chess.rank.rook.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


# ======================# RANK_DESIGNATION #======================#
class NotRookDesignationException(RookDesignation, RankDesignationException):
    """Raised when a tested designation is not a Rook's."""
    ERROR_CODE = "ROOK_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct Rook designation."


# ======================# RANK_ID EXCEPTION #======================#
class NotRookIdException(RookException, RankIdException):
    """Raised when a tested designation is not a Rook's."""
    ERROR_CODE = "ROOK_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Rook id."


# ======================# RANK_NAME EXCEPTION #======================#
class NotRookNameException(RookException, RankNameException):
    """Raised when a tested name is not a Rook's."""
    ERROR_CODE = "ROOK_NAME_ERROR"
    DEFAULT_MESSAGE = "Not the correct Rook name."


# ======================# RANK_QUOTA EXCEPTION #======================#
class NotRookQuotaException(RookException, TeamQuotaException):
    """Raised when a tested quota is not a Rook's."""
    ERROR_CODE = "ROOK_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Not the correct Rook quota for a team."


# ======================# RANK_RANSOM EXCEPTION #======================#
class NotRookRansomException(RookException, RankRansomException):
    """Raised when a tested ransom is not a Rook's."""
    ERROR_CODE = "ROOK_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Not the correct Rook ransom."














