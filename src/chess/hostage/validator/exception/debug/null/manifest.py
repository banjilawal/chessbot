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
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

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
    ERROR_CODE = "NULL_HOSTAGE_ERROR"
    DEFAULT_MESSAGE = "Hostage validation failed: The candidate was null."