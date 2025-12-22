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
    1.  Indicate an entity, method, or operation required a String with some characters but got one that
        only had whitespace.

    # PARENT:
        *   VoidStringException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "WHITE_SPACE_STRING_ERROR"
    DEFAULT_MESSAGE = (
        "Got a String that only had whitespace. A String must have some characters."
    )