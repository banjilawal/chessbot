# src/chess/system/identity/collision.py

"""
Module: chess.system.identity.exception
Author: Banji Lawal
Created: 2025-09-17
version: 1.0.0
"""

from chess.system import NullException, ValidationException

__all__ = [
    "IdentityException",
    "InvalidIdentityException",
    "IdentityNullException",
]

from chess.system.err import ChessException


class IdentityException(ChessException):
    """Catchall Exception for IdValidator when a candidate fails a sanity check."""
    ERROR_CODE = "IDENTITY_PROPERTY_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Identity property failed validation."

class InvalidIdentityException(IdentityException, ValidationException):
    """Catchall Exception for IdValidator when a candidate fails a sanity check."""
    ERROR_CODE = "IDENTITY_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Identity failed validation."


class IdentityNullException(IdentityException, NullException):
    """Catchall Exception for IdValidator when a candidate fails a sanity check."""
    ERROR_CODE = "IDENTITY_PROPERTY_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Identity property failed validation."
