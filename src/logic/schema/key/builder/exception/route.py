# src/logic/schema/key/builder/exception/route.py

"""
Module: logic.schema.key.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_SCHEMA_KEY_BUILD_ROUTE EXCEPTION #======================#
    "SchemaKeyBuildRouteException",
]

from logic.schema import SchemaKeyException
from logic.system import ExecutionRouteException


# ======================# NO_SCHEMA_KEY_BUILD_ROUTE EXCEPTION #======================#
class SchemaKeyBuildRouteException(SchemaKeyException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SchemaKey build failed because there was no build route for the Schema key.

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
    ERR_CODE = "NO_SCHEMA_KEY_BUILD_ROUTE_EXCEPTION"
    MSG = "SchemaKey build failed: No build path existed for the Schema key."