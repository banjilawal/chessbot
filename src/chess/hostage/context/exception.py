# src/chess/hostage/context/exception.py

"""
Module: chess.hostage.context.exception
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.hostageManifest import HostageManifestException
from chess.system import ContextException

__all__ = [
    # ======================# HOSTAGE_MANIFEST_CONTEXT EXCEPTION #======================#
    "HostageManifestContextException",
]


# ======================# HOSTAGE_MANIFEST_CONTEXT EXCEPTION #======================#
class HostageManifestContextException(HostageManifestException, ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by HostageManifestContext objects.

    # PARENT:
        *   HostageManifestException
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_MANIFEST_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "HostageManifestContext raised an exception."