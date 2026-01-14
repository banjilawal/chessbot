# src/chess/schema/key/validator/exception/debug/route.py

"""
Module: chess.schema.key.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_SCHEMA_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "SchemaKeyValidationRouteException",
]

from chess.schema import SchemaKeyException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_SCHEMA_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class SchemaKeyValidationRouteException(SchemaKeyException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SchemaKey validation failed because there was no build route for the SchemaKey key.

    # PARENT:
        *   SchemaKeyException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SCHEMA_KEY_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SchemaKey validation failed: No validation route was provided for the Schema attribute."