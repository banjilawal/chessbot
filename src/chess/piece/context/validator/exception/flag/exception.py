# src/chess/piece/context/validator/exception/flag/exception.py

"""
Module: chess.piece.context.validator.exception.flag.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BoundsException
from chess.piece import InvalidPieceContextException

__all__ = [
    #========================= PIECE_CONTEXT FLAG EXCEPTIONS =========================#
    "NoPieceContextFlagSetException",
    "ExcessivePieceContextFlagsSetException"
]


#========================= PIECE_CONTEXT FLAG EXCEPTIONS =========================#
class NoPieceContextFlagSetException(InvalidPieceContextException, BoundsException):
    """Raised if no PieceContext was selected."""
    ERROR_CODE = "NO_PIECE_CONTEXT_FLAG_SET_ERROR"
    DEFAULT_MESSAGE = "One and only one, PieceContext flag must be set."


class ExcessivePieceContextFlagsSetException(InvalidPieceContextException, BoundsException):
    """Raised if too many PieceContext flags were set."""
    ERROR_CODE = "PIECE_CONTEXT_MAX_PARAM_ERROR"
    DEFAULT_MESSAGE = "Only one PieceContext flag can be set."