# src/logic/manifest/validation/exception/debug/manifest.py

"""
Module: logic.manifest.validation.exception.debug.manifest
Author: Banji Lawal
Created: 2026-01-18
"""

__all__ = [
    # ======================# NULL_HOSTAGE EXCEPTION #======================#
    "NullHostageException",
]

from logic.system import NullException
from logic.hostage import HostageException


# ======================# NULL_HOSTAGE EXCEPTION #======================#
class NullHostageException(HostageDebugException, NullException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    A failing ValidationResult was returned because the rank was null.

    Super Class:
        *   NullException
        *   HostageException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_HOSTAGE_EXCEPTION"
    MSG = "Hostage validation failed: The rank was null."