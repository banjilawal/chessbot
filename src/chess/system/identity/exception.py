# src/chess/system/identity/exception.py

"""
Module: chess.system.identity.exception
Author: Banji Lawal
Created: 2025-09-17
version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    "InvalidIdentityParamException",
]


class InvalidIdentityParamException(ValidationException):
    """Catchall Exception for IdValidator when a candidate fails a sanity check."""
    ERROR_CODE = "IDENTITY_PROPERTY_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Identity property failed validation."