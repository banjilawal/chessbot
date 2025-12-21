# src/chess/system/text/exception/void/null.py

"""
Module: chess.system.text.exception.void.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


__all__ = [
    # ======================# NULL_STRING EXCEPTION #======================#
    "NullStringException",
]


#======================# NULL_STRING EXCEPTION #======================#
class NullStringException(VoidStringException, NullException):
    """Raised if an entity, method, or operation requires a String but gets either whitespace, null, or an empty string instead.her null or an empty string"""
    ERROR_CODE = "NULL_STRING_ERROR"
    DEFAULT_MESSAGE = (
        "Got a String that was either whitespace, null, or an empty string. A String must be non-null and non-empty."
    )