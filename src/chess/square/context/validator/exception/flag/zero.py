# src/chess/square/context/validator/exception/flag/__init__.py

"""
Module: chess.square.context.validator.exception.flag.__init__
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import BoundsException
from chess.square import InvalidSquareContextException

__all__ = [
    "ZeroSquareContextFlagsException",
    "ExcessiveSquareContextFlagsSetException"
]

class ZeroSquareContextFlagsException(
    InvalidSquareContextException,
    BoundsException
):
    """Raised if no SquareContext was selected."""
    ERROR_CODE = "NO_SQUARE_CONTEXT_FLAG_SET_ERROR"
    DEFAULT_MESSAGE = "One SquareContext flag must be set."
