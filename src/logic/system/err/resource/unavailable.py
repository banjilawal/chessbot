# src/logic/system/err/resource/unavailable.py

"""
Module: logic.system.err.resource.unavailable
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from logic.system import ChessException

__all__ = [
    # ======================# RESOURCE_UNAVAILABLE EXCEPTION #======================#
    "ResourceUnavailableException"
]

# ======================# RESOURCE_UNAVAILABLE EXCEPTION #======================#
class ResourceUnavailableException(ChessException):
    """
    # ROLE: Error Tracing, Debugging, Super Exception

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
    ERR_CODE = "RESOURCE_UNAVAILABLE_EXCEPTION"
    MSG = "Resource is unavailable."
