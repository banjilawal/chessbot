# src/chess/system/lookup/forward/exception.py

"""
Module: chess.system.lookup.forward.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import LookupFailedException

__all__ = [
    # ======================# FORWARD_LOOKUP_FAILED EXCEPTION #======================#
    "ForwardLookupFailedException",
]


# ======================# FORWARD_LOOKUP_FAILED EXCEPTION #======================#
class ForwardLookupFailedException(LookupFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by ForwardLookup objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of a ForwardLookup method.

    # PARENT:
        *   LookupException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORWARD_LOOKUP_FAILED_ERROR"
    DEFAULT_MESSAGE = "Forward lookup failed."