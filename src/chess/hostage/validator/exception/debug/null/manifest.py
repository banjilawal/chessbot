# src/chess/manifest/validator/exception/debug/manifest.py

"""
Module: chess.manifest.validator.exception.debug.manifest
Author: Banji Lawal
Created: 2026-01-18
"""

__all__ = [
    # ======================# NULL_HOSTAGE_MANIFEST EXCEPTION #======================#
    "NullHostageManifestException",
]

from chess.system import NullException
from chess.hostage import HostageManifestException


# ======================# NULL_HOSTAGE_MANIFEST EXCEPTION #======================#
class NullHostageManifestException(HostageManifestDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the validation candidate was null.

    # PARENT:
        *   NullException
        *   HostageManifestException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_HOSTAGE_MANIFEST_ERROR"
    DEFAULT_MESSAGE = "HostageManifest validation failed: The candidate was null."