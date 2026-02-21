# src/chess/hostage/context/exception.py

"""
Module: chess.hostage.context.exception
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.hostage import HostageManifestException
from chess.system import ContextException

__all__ = [
    # ======================# HOSTAGE_MANIFEST_CONTEXT EXCEPTION #======================#
    "CaptivityContextException",
]


# ======================# HOSTAGE_MANIFEST_CONTEXT EXCEPTION #======================#
class CaptivityContextException(HostageManifestException, ContextException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by CaptivityContext objects.

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
    DEFAULT_ERROR_CODE = "CaptivityContext raised an exception."