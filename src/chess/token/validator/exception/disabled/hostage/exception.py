# src/chess/piece/validator/exception/disabled/hostage/exception.py

"""
Module: chess.piece.validator.exception.disabled.hostage.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.piece import PieceException

__all__ = []




class CapturedPieceException(PieceException):
    """Raised when trying to use a piece captured by the enemy"""
    ERROR_CODE = "CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "Token has been captured by the enemy."