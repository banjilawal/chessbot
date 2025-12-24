# src/chess/coord/validator/exception/flag/excess.py

"""
Module: chess.coord.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.coord import InvalidCoordContextException

__all__ = [
    # ========================= EXCESSIVE_COORD_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveCoordContextFlagsException"
]


# ========================= EXCESSIVE_COORD_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveCoordContextFlagsException(InvalidCoordContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  more than one CoordContext flag was enabled. Only one Coord attribute-value-tuple can be used in
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidCoordContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_COORD_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = (
        "Excessive CoordContext flags were set. an Coord search can only use one-and-only "
        "map flag at a time."
    )