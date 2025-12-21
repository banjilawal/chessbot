# src/chess/piece/map/validator/exception/flag/excess.py

"""
Module: chess.piece.map.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.piece import InvalidPieceContextException

__all__ = [
    # ========================= EXCESSIVE_PIECE_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessivePieceContextFlagsException"
]


# ========================= EXCESSIVE_PIECE_CONTEXT_FLAG EXCEPTION =========================#
class ExcessivePieceContextFlagsException(InvalidPieceContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates more than one PieceContext flag was enabled. Only one Piece attribute-value-tuple can be used in
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidPieceContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_PIECE_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = (
        "Excessive PieceContext flags were set. an Piece search can only use one-and-only "
        "map flag at a time."
    )