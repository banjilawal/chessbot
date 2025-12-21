# src/chess/system/lookup/reverse/exception.py

"""
Module: chess.system.lookup.reverse.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import LookupFailedException

__all__ = [
    # ======================# REVERSE_LOOKUP_FAILED EXCEPTION #======================#
    "ReverseLookupFailedException",
]


# ======================# REVERSE_LOOKUP_FAILED EXCEPTION #======================#
class ReverseLookupFailedException(LookupFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by ReverseLookup objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of a ReverseLookup method.

    # PARENT:
        *   LookupException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "REVERSE_LOOKUP_FAILED_ERROR"
    DEFAULT_MESSAGE = "Reverse lookup failed."