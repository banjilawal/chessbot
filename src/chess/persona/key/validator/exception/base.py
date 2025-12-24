# src/chess/persona/key/validator/exception/base.py

"""
Module: chess.persona.key.validator.exception.base
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.catalog import PersonaSuperKeyException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# PERSONA_SUPER_KEY_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidPersonaSuperKeyException",
]


# ======================# PERSONA_SUPER_KEY_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidPersonaSuperKeyException(PersonaSuperKeyException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised PersonaSuperKey validation.
    2.  Wrap an exception that hits the try-finally-block in PersonaSuperKeyValidator methods.

    # PARENT:
        *   PersonaSuperKeyException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_SUPER_KEY_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "PersonaSuperKey validation failed."