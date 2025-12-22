# src/chess/schema/key/validator/exception/base.py

"""
Module: chess.schema.key.validator.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaSuperKeyException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# SCHEMA_SUPER_KEY_VALIDATION EXCEPTION #======================#
    "InvalidSchemaSuperKeyException",
]


# ======================# SCHEMA_SUPER_KEY_VALIDATION EXCEPTION #======================#
class InvalidSchemaSuperKeyException(SchemaSuperKeyException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate a candidate failed a SchemaSuperKey validation test.
    2.  Wrap an exception that hits the try-finally block of a SchemSuperKeyValidator method.
    
    # PARENT:
        *   SchemaSuperKeyException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_SUPER_KEY_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "SchemaSuperKey validation failed."