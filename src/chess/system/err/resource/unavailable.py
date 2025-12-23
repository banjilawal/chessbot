# src/chess/system/err/resource/unavailable.py

"""
Module: chess.system.err.resource.unavailable
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


# ======================# RESOURCE_UNAVAILABLE EXCEPTION #======================#
class ResourceUnavailableException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a resource a client needs is unavailable.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "RESOURCE_UNAVAILABLE_ERROR"
    DEFAULT_MESSAGE = "Resource is unavailable."
