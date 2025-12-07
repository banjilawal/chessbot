# src/chess/square/context/validator/exception/null/exception.py

"""
Module: chess.square.context.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import NullException
from chess.square import InvalidSquareContextException


# ========================= NULL SQUARE_CONTEXT EXCEPTIONS =========================#
class NullSquareContextException(
    InvalidSquareContextException,
    NullException
):
    """Raised if an entity, method, or operation requires SquareContext but gets null instead."""
    ERROR_CODE = "NULL_SQUARE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "SquareContext cannot be null."