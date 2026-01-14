# src/chess/schema/key/builder/exception/route.py

"""
Module: chess.schema.key.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_SCHEMA_KEY_BUILD_ROUTE EXCEPTION #======================#
    "SchemaKeyBuildRouteException",
]

from chess.schema import SchemaSuperKeyException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_SCHEMA_KEY_BUILD_ROUTE EXCEPTION #======================#
class SchemaKeyBuildRouteException(SchemaSuperKeyException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SchemaKey build failed because there was no build route for the Schema key.

    # PARENT:
        *   SchemaSuperKeyException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SCHEMA_KEY_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SchemaKey build failed: No build path existed for the Schema key."