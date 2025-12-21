# src/chess/system/text/exception/void/base.py

"""
Module: chess.system.text.exception.void.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


__all__ = [
    # ======================# NULL_VOID_STRING EXCEPTION #======================#
    "VoidStringException",
]


#======================# NULL_VOID_STRING EXCEPTION #======================#
class VoidStringException(InvalidStringException, NullException):
    """Raised if an entity, method, or operation requires a String but gets either whitespace, null, or an empty string instead.her null or an empty string"""
    ERROR_CODE = "NULL_VOID_STRING_ERROR"
    DEFAULT_MESSAGE = (
        "Got a String that was either whitespace, null, or an empty string. A String must be non-null and non-empty."
    )