# src/chess/piece/context/validator/exception/flag/zero.py

"""
Module: chess.piece.context.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BoundsException
from chess.piece import InvalidPieceContextException

__all__ = [
    #========================= PIECE_CONTEXT FLAG EXCEPTION =========================#
    "ZeroPieceContextFlagsException",
]


#========================= PIECE_CONTEXT FLAG EXCEPTION =========================#
class ZeroPieceContextFlagsException(InvalidPieceContextException, BoundsException):
    """Raised if no PieceContext was selected."""
    ERROR_CODE = "NO_PIECE_CONTEXT_FLAG_SET_ERROR"
    DEFAULT_MESSAGE = "One and only one, PieceContext flag must be set."
