# src/logic/schema/key/validation/exception/debug/route.py

"""
Module: logic.schema.key.validation.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_SCHEMA_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "SchemaKeyValidationRouteException",
]

from catalog.schema import SchemaKeyException
from system import ExecutionRouteException


# ======================# NO_SCHEMA_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class SchemaKeyValidationRouteException(SchemaKeyException, ExecutionRouteException):
    """
    Role:Fallback Result, Debugging

    Responsibilities:
    1.  Indicate that the SchemaKey validation failed because there was no build route for the SchemaKey key.

    Super Class:
        *   SchemaKeyException
        *   ExecutionRouteException

    # PROVIDES
    None


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_SCHEMA_KEY_VALIDATION_ROUTE_EXCEPTION"
    MSG = "SchemaKey validation failed: No validation route was provided for the Schema attribute."