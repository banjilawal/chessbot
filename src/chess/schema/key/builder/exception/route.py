# src/chess/schema/key/builder/exception/route.py

"""
Module: chess.schema.key.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_SCHEMA_KEY_BUILD_ROUTE EXCEPTION #======================#
    "SchemaKeyBuildRouteException",
]

from chess.schema import SchemaKeyException
from chess.system import NoExecutionRouteException


# ======================# NO_SCHEMA_KEY_BUILD_ROUTE EXCEPTION #======================#
class SchemaKeyBuildRouteException(SchemaKeyException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SchemaKey build failed because there was no build route for the Schema key.

    # PARENT:
        *   SchemaKeyException
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_SCHEMA_KEY_BUILD_ROUTE_ERROR"
    MSG = "SchemaKey build failed: No build path existed for the Schema key."