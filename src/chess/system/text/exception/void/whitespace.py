# src/chess/system/text/exception/void/whitespace.py

"""
Module: chess.system.text.exception.void.whitespace
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import VoidStringException

__all__ = [
    # ======================# WHITE_SPACE_STRING EXCEPTION #======================#
    "WhiteSpaceStringException",
]




#======================# WHITE_SPACE_STRING EXCEPTION #======================#
class WhiteSpaceStringException(VoidStringException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates a value being passed a Coord or Vector component is larger than the Board's dimension.

    # PARENT:
        *   InvalidNumberException
        *   BoundsException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    """Raised if an entity, method, or operation requires a String but gets either whitespace, null, or an empty string instead.her null or an empty string"""
    ERROR_CODE = "WHITE_SPACE_STRING_ERROR"
    DEFAULT_MESSAGE = (
        "Got a String that was either whitespace, null, or an empty string. A String must be non-null and non-empty."
    )