# src/chess/piece/map/validator/exception/flag/zero.py

"""
Module: chess.piece.map.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.piece import InvalidPieceContextException

__all__ = [
    # ========================= ZERO_PIECE_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroPieceContextFlagsException"
]


# ========================= ZERO_PIECE_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroPieceContextFlagsException(InvalidPieceContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates no PieceContext flag was enabled. One and only one Piece attribute-value-tuple is required for
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
    ERROR_CODE = "ZERO_PIECE_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "Zero PieceContext flags were set. Cannot search for Pieces if one-and_oly-one "
        "map flag is enabled."
    )
