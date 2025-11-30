# src/chess/rank/queen/exception.py

"""
Module: chess.rank.queen.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


# ======================# RANK_DESIGNATION #======================#
class NotQueenDesignationException(QueenException, RankDesignationException):
    """Raised when a tested designation is not a Queen's."""
    ERROR_CODE = "QUEEN_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct Queen designation."


# ======================# RANK_ID EXCEPTIONS #======================#
class NotQueenIdException(QueenException, RankIdException):
    """Raised when a tested designation is not a Queen's."""
    ERROR_CODE = "Queen_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Queen id."