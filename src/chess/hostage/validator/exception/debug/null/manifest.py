# src/chess/manifest/validator/exception/debug/manifest.py

"""
Module: chess.manifest.validator.exception.debug.manifest
Author: Banji Lawal
Created: 2026-01-18
"""

__all__ = [
    # ======================# NULL_HOSTAGE EXCEPTION #======================#
    "NullHostageException",
]

from chess.system import NullException
from chess.hostage import HostageException


# ======================# NULL_HOSTAGE EXCEPTION #======================#
class NullHostageException(HostageDebugException, NullException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the candidate was null.

    # PARENT:
        *   NullException
        *   HostageException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_HOSTAGE_EXCEPTION"
    MSG = "Hostage validation failed: The candidate was null."