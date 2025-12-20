# src/chess/piece/number_bounds_validator/exception/exception.py

"""
Module: chess.piece.number_bounds_validator.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.piece import PieceException
from chess.system import  ValidationException

__all__ = [
    #======================# PIECE VALIDATION EXCEPTION #======================#
    "InvalidPieceException",
]


#======================# PIECE VALIDATION EXCEPTION #======================#
class InvalidPieceException(PieceException, ValidationException):
    """
    Catchall Exception for PieceValidator when a candidate fails a sanity check."""
    ERROR_CODE = "PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Piece validation failed."



