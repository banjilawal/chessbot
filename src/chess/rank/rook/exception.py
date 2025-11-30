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


# ======================# RANK_ID EXCEPTIONS #======================#
class NotRookIdException(RookException, RankIdException):
    """Raised when a tested designation is not a Rook's."""
    ERROR_CODE = "ROOK_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Rook id."










