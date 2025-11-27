# src/chess/piece/validator/exception/exception.py

"""
Module: chess.piece.validator.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.piece import PieceException
from chess.system import  ValidationException

__all__ = [
    # ======================# PIECE VALIDATION EXCEPTION SUPER CLASS #======================#
    "InvalidPieceException",
]


# ======================# PIECE VALIDATION EXCEPTION SUPER CLASS #======================#
class InvalidPieceException(PieceException, ValidationException):
    """
    Catchall Exception for PieceValidator when a validation candidate fails a sanity check. Super
    class of all Piece validation exceptions.
    """
    ERROR_CODE = "PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Piece validation failed."



