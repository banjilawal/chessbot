# src/chess/token/exception.py

"""
Module: chess.token.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ContextException

__all__ = [
    "TokenContextException",
]

class TokenContextException(ContextException):
    ERROR_CODE = "PIECE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "PieceContext raised an exception."