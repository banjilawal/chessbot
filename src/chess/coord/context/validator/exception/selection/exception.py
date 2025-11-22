# src/chess/coord/context/validator/exception/selection/exception.py

"""
Module: chess.coord.context.validator.exception.selection.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from chess.system import BoundsException
from chess.coord import InvalidCoordContextException


__all__ = [
    "NoCoordContextFlagSetException",
    "TooManyCoordContextFlagsSetException"
]

class NoCoordContextFlagSetException(InvalidCoordContextException, BoundsException):
    """Raised if no CoordContext was selected."""
    ERROR_CODE = "NO_COORD_CONTEXT_FLAG_SET_ERROR"
    DEFAULT_MESSAGE = "At least one CoordContext flag must be set."


class TooManyCoordContextFlagsSetException(InvalidCoordContextException, BoundsException):
    """Raised if too many CoordContext flags were set."""
    ERROR_CODE = "SEARCH_CONTEXT_MAX_PARAM_ERROR"
    DEFAULT_MESSAGE = "Only one CoordContext flag can be set."
