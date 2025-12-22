# src/chess/system/lookup/service/exception.py

"""
Module: chess.system.lookup.service.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


__all__ = [
    # ======================# LOOKUP_SERVICE EXCEPTION #======================#
    "LookupServiceException",
]

from chess.system import LookupException


# ======================# LOOKUP_SERVICE EXCEPTION #======================#
class LookupServiceException(LookupException, ContextServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by ServiceLookup objects.
    2.  Wrap an exception that hit the try-finally block of a ServiceLookup method.

    # PARENT:
        *   LookupException
        *   ContextServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "LOOKUP_SERVICE_ERROR"
    DEFAULT_MESSAGE = "LookupService raised an exception."
