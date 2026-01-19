# src/chess/manifest/validator/exception/null.py

"""
Module: chess.manifest.validator.exception.null
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# NULL_HOSTAGE_MANIFEST EXCEPTION #======================#
    "NullHostageManifestException",
]

from chess.system import NullException
from chess.hostage import HostageManifestException


# ======================# NULL_HOSTAGE_MANIFEST EXCEPTION #======================#
class NullHostageManifestException(HostageManifestException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that an entity, method, or operation that required a HostageManifest but got null instead.

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
    DEFAULT_MESSAGE = "HostageManifest cannot be null."