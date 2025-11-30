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


# ======================# RANK_NAME INCONSISTENCY EXCEPTIONS #======================#
class NotQueenNameException(QueenException, RankNameException):
    """Raised when a tested name is not a Queen's."""
    ERROR_CODE = "Queen_NAME_ERROR"
    DEFAULT_MESSAGE = "Not the correct Queen name."


# ======================# RANK_QUOTA INCONSISTENCY EXCEPTIONS #======================#
class NotQueenQuotaException(QueenException, TeamQuotaException):
    """Raised when a tested quota is not a Queen's."""
    ERROR_CODE = "QUEEN_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Not the correct Queen quota for a team."


# ======================# RANK_RANSOM EXCEPTION #======================#
class NotQueenRansomException(QueenException, RankRansomException):
    """Raised when a tested ransom is not a Queen's."""
    ERROR_CODE = "QUEEN_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Not the correct Queen ransom."