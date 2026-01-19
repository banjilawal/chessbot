# src/chess/manifest/validator/exception/debug/suicide.py

"""
Module: chess.manifest.validator.exception.debug.suicide
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# TOKEN_CANNOT_CAPTURE_ITSELF EXCEPTION #======================#
    "TokenCannotCaptureItselfException",
]


from chess.hostage import HostageManifestException


# ======================# TOKEN_CANNOT_CAPTURE_ITSELF EXCEPTION #======================#
class TokenCannotCaptureItselfException(HostageManifestException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that an entity, method, or operation that required a HostageManifest but got null instead.

    # PARENT:
        *   HostageManifestException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_CANNOT_CAPTURE_ITSELF_ERROR"
    DEFAULT_MESSAGE = "HostageManifest validation failed: TheVictor and Captor cannot be the same."