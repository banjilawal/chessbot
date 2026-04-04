# src/logic/system/err/resource/unavailable.py

"""
Module: logic.system.err.resource.unavailable
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from system import ChessException

__all__ = [
    # ======================# RESOURCE_UNAVAILABLE EXCEPTION #======================#
    "ResourceUnavailableException"
]

# ======================# RESOURCE_UNAVAILABLE EXCEPTION #======================#
class ResourceUnavailableException(ChessException):
    """
    Role:Error Tracing, Debugging, Super Exception

    Responsibilities:
    1.  Indicate that a resource a client needs is unavailable.

    Super Class:
        *   ChessException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "RESOURCE_UNAVAILABLE_EXCEPTION"
    MSG = "Resource is unavailable."
