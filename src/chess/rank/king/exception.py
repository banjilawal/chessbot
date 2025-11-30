# src/chess/rank/king/exception.py

"""
Module: chess.rank.king.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

# ======================# RANK_DESIGNATION #======================#
class NotKingDesignationException(KingException, RankDesignationException):
    """Raised when a tested designation is not a King's."""
    ERROR_CODE = "KING_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct King designation."


# ======================# RANK_ID EXCEPTIONS #======================#
class NotKingIdException(KingException, RankIdException):
    """Raised when a tested designation is not a King's."""
    ERROR_CODE = "KING_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct King id."