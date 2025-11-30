# src/chess/rank/bishop/exception.py

"""
Module: chess.rank.bishop.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


# ======================# RANK_DESIGNATION #======================#
class NotBishopDesignationException(BishopException, RankDesignationException):
    """Raised when a tested designation is not a Bishop's."""
    ERROR_CODE = "BISHOP_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct Bishop designation."


# ======================# RANK_ID EXCEPTIONS #======================#
class NotBishopIdException(BishopException, RankIdException):
    """Raised when a tested designation is not a Bishop's."""
    ERROR_CODE = "BISHOP_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Bishop id."