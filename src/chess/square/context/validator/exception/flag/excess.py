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
    "ExcessiveSquareContextFlagsException"
]


class ExcessiveSquareContextFlagsException(
    InvalidSquareContextException,
    BoundsException
):
    """Raised if too many CoordContext flags were set."""
    ERROR_CODE = "SQUARE_CONTEXT_MAX_PARAM_ERROR"
    DEFAULT_MESSAGE = "Only one SquareContext flag can be set."