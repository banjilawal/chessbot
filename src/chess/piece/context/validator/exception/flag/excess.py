# src/chess/piece/context/validator/exception/flag/excess.py

"""
Module: chess.piece.context.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.piece import InvalidPieceContextException

__all__ = [
    #========================= PIECE_CONTEXT FLAG EXCEPTION =========================#
    "ExcessivePieceContextFlagsException"
]


#========================= PIECE_CONTEXT FLAG EXCEPTION =========================#
class ExcessivePieceContextFlagsException(InvalidPieceContextException, ContextFlagCountException):
    """Raised if too many PieceContext flags were set."""
    ERROR_CODE = "PIECE_CONTEXT_MAX_PARAM_ERROR"
    DEFAULT_MESSAGE = "Only one PieceContext flag can be set."