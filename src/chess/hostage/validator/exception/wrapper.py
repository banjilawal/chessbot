# src/chess/hostage/validator/exception/wrapper.py

"""
Module: chess.hostage.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-11-19
"""

from chess.hostage import HostageManifestException
from chess.system import ValidationException

__all__ = [
    # ======================# HOSTAGE_MANIFEST_VALIDATION_FAILURE EXCEPTION #======================#
    "HostageManifestValidationException",
]


# ======================# HOSTAGE_MANIFEST_VALIDATION_FAILURE EXCEPTION #======================#
class HostageManifestValidationException(HostageManifestException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a HostageManifest. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   HostageManifestException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "HostageManifest validation failed."