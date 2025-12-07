# src/chess/piece/context/validator/exception/base.py

"""
Module: chess.piece.context.validator.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.system import ContextException


__all__ = [
    "InvalidPieceContextException"
]

class InvalidPieceContextException(ContextException):
    ERROR_CODE = "PIECE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "PieceContext raised an exception."