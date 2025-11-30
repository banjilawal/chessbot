# src/chess/rank/pawn/exception.py

"""
Module: chess.rank.pawn.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""





# ======================# RANK_DESIGNATION EXCEPTION #======================#
class NotPawnDesignationException(PawnException, RankDesignationException):
    """Raised when a tested designation is not a Pawn's."""
    ERROR_CODE = "ROOK_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn designation."


# ======================# RANK_ID EXCEPTION #======================#
class NotPawnIdException(PawnException, RankIdException):
    """Raised when a tested designation is not a Pawn's."""
    ERROR_CODE = "PAWN_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn id."


# ======================# RANK_NAME EXCEPTION #======================#
class NotPawnNameException(PawnException, RankNameException):
    """Raised when a tested name is not a Pawn's."""
    ERROR_CODE = "PAWN_NAME_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn name."


# ======================# TEAM_QUOTA EXCEPTION #======================#
class NotPawnQuotaException(PawnException, TeamQuotaException):
    """Raised when a tested quota is not a Pawn's."""
    ERROR_CODE = "PAWN_QUOTA_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn quota for a team."


# ======================# RANK_RANSOM EXCEPTION #======================#
class NotPawnRansomException(PawnException, RankRansomException):
    """Raised when a tested quota is not a Pawn's."""
    ERROR_CODE = "PAWN_RANSOM_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn ransom."