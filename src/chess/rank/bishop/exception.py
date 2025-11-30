# src/chess/rank/bishop/exception.py

"""
Module: chess.rank.bishop.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


# ======================# RANK_DESIGNATION EXCEPTION #======================#
class NotBishopDesignationException(BishopException, RankDesignationException):
    """Raised when a tested designation is not a Bishop's."""
    ERROR_CODE = "BISHOP_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct Bishop designation."


# ======================# RANK_ID EXCEPTIONS #======================#
class NotBishopIdException(BishopException, RankIdException):
    """Raised when a tested designation is not a Bishop's."""
    ERROR_CODE = "BISHOP_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Bishop id."


# ======================# RANK_NAME EXCEPTIONS #======================#
class NotBishopNameException(BishopException, RankNameException):
    """Raised when a tested name is not a Bishop's."""
    ERROR_CODE = "BISHOP_NAME_ERROR"
    DEFAULT_MESSAGE = "Not the correct Bishop name."


# ======================# RANK_QUOTA INCONSISTENCY EXCEPTIONS #======================#
class NotBishopQuotaException(BishopException, TeamQuotaException):
    """Raised when a tested quota is not a Bishop's."""
    ERROR_CODE = "BISHOP_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Not the correct Bishop quota for a team."


# ======================# RANK_RANSOM EXCEPTION #======================#
class NotBishopRansomException(BishopException, RankRansomException):
    """Raised when a tested ransom is not a Bishop's."""
    ERROR_CODE = "BISHOP_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Not the correct Bishop ransom."











