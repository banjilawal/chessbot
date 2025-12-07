# src/chess/piece/context/validator/null/exception.py

"""
Module: chess.piece.context.validator.null.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import NullException
from chess.piece import InvalidPieceContextException

__all__ = [
    # ========================= NULL PIECE_CONTEXT EXCEPTIONS =========================#
    "NullPieceContextException"
]


# ========================= NULL PIECE_CONTEXT EXCEPTIONS =========================#
class NullPieceContextException(InvalidPieceContextException, NullException):
    """Raised if an entity, method, or operation requires PieceContext but gets null instead."""
    ERROR_CODE = "NULL_PIECE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "PieceContext cannot be null."