# src/chess/piece/validator/exception/disabled/placement/exception.py

"""
Module: chess.piece.validator.exception.disabled.placement.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.piece import PieceException
from chess.layout import LayoutException


__all__ = [
    "PieceLayoutNotActivatedException",
]




class PieceLayoutNotActivatedException(PieceException, LayoutException):
    """Raised when a Piece has not been activated to be placed on the board."""
    ERROR_CODE = "PIECE_LAYOUT_NOT_ACTIVATED_ERROR"
    DEFAULT_MESSAGE = (
        "Piece.layout has not been activated. The piece has not been placed on the board."
    )