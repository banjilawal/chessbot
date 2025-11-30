# src/chess/rank/pawn/exception.py

"""
Module: chess.rank.pawn.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""





# ======================# RANK_DESIGNATION #======================#
class NotPawnDesignationException(PawnException, RankDesignationException):
    """Raised when a tested designation is not a Pawn's."""
    ERROR_CODE = "ROOK_DESIGNATION_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn designation."


# ======================# RANK_ID EXCEPTIONS #======================#
class NotPawnIdException(PawnException, RankIdException):
    """Raised when a tested designation is not a Pawn's."""
    ERROR_CODE = "PAWN_ID_ERROR"
    DEFAULT_MESSAGE = "Not the correct Pawn id."