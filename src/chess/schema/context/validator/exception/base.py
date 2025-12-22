# src/chess/schema/map/validator/exception/base.py

"""
Module: chess.schema.map.validator.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema.map import SchemaSuperKeyException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# INVALID_SCHEMA_SUPER_KEY EXCEPTION #======================#
    "InvalidSchemaSuperKeyException",
]


# ======================# INVALID_SCHEMA_SUPER_KEY EXCEPTION #======================#
class InvalidSchemaSuperKeyException(SchemaSuperKeyException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wraps an exception that hits the try-finally-block in SchemaSuperKeyValidator methods.

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