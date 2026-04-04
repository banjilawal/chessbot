# src/logic/manifest/validation/exception/debug/occupant.py

"""
Module: logic.manifest.validation.exception.debug.toke
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# TOKEN_CANNOT_CAPTURE_ITSELF EXCEPTION #======================#
    "TokenCannotCaptureItselfException",
]


from model.hostage import HostageException


# ======================# TOKEN_CANNOT_CAPTURE_ITSELF EXCEPTION #======================#
class TokenCannotCaptureItselfException(HostageException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that an entity, method, or operation that required a Hostage but got null instead.

    Super Class:
        *   HostageException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_CANNOT_CAPTURE_ITSELF_EXCEPTION"
    MSG = "Hostage validation failed: TheVictor and Captor cannot be the same."