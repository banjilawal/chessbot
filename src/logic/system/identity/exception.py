# src/logic/system/identity/collision.py

"""
Module: logic.system.identity.exception
Author: Banji Lawal
Created: 2025-09-17
version: 1.0.0
"""

from logic.system import NullException, ValidationException

__all__ = [
    "IdentityException",
    "InvalidIdentityException",
    "IdentityNullException",
]

from logic.system.err import ChessException


class IdentityException(ChessException):
    """Super Exception for IdValidator when a candidate fails a sanity check."""
    ERR_CODE = "IDENTITY_PROPERTY_VALIDATION_EXCEPTION"
    MSG = "Identity property failed validation."

class InvalidIdentityException(IdentityException, ValidationException):
    """Super Exception for IdValidator when a candidate fails a sanity check."""
    ERR_CODE = "IDENTITY_VALIDATION_EXCEPTION"
    MSG = "Identity failed validation."


class IdentityNullException(IdentityException, NullException):
    """Super Exception for IdValidator when a candidate fails a sanity check."""
    ERR_CODE = "IDENTITY_PROPERTY_VALIDATION_EXCEPTION"
    MSG = "Identity property failed validation."
