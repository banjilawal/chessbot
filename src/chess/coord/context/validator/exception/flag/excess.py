# src/chess/coord/context/validator/exception/flag/excess.py

"""
Module: chess.coord.context.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from chess.system import BoundsException
from chess.coord import InvalidCoordContextException


__all__ = [
    # ========================= EXCESSIVE_COORD_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveCoordContextFlagsSetException"
]

# ========================= EXCESSIVE_COORD_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveCoordContextFlagsSetException(InvalidCoordContextException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates more than one CoordContext flag was enabled. Only one Coord attribute-value tuple can be used in
        a search.

    # PARENT:
        *   BoundsException
        *   InvalidCoordContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_COORD_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "Excessive CoordContext flags were set. Only one CoordContext flag is allowed."
