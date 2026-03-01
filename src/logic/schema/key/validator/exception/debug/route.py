# src/logic/schema/key/validator/exception/debug/route.py

"""
Module: logic.schema.key.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_SCHEMA_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "SchemaKeyValidationRouteException",
]

from logic.schema import SchemaKeyException
from logic.system import ExecutionRouteException


# ======================# NO_SCHEMA_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class SchemaKeyValidationRouteException(SchemaKeyException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SchemaKey validation failed because there was no build route for the SchemaKey key.

    # PARENT:
        *   SchemaKeyException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_SCHEMA_KEY_VALIDATION_ROUTE_EXCEPTION"
    MSG = "SchemaKey validation failed: No validation route was provided for the Schema attribute."