# src/logic/manifest/validator/exception/debug/occupant.py

"""
Module: logic.manifest.validator.exception.debug.toke
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# TOKEN_CANNOT_CAPTURE_ITSELF EXCEPTION #======================#
    "TokenCannotCaptureItselfException",
]


from logic.hostage import HostageException


# ======================# TOKEN_CANNOT_CAPTURE_ITSELF EXCEPTION #======================#
class TokenCannotCaptureItselfException(HostageException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that an entity, method, or operation that required a Hostage but got null instead.

    # PARENT:
        *   HostageException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_CANNOT_CAPTURE_ITSELF_EXCEPTION"
    MSG = "Hostage validation failed: TheVictor and Captor cannot be the same."