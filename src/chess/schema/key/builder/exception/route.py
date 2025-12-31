# src/chess/schema/key/builder/exception/route.py

"""
Module: chess.schema.key.builder.exception.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaSuperKeyException
from chess.system import UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_SCHEMA_SUPER_KEY_BUILD_ROUTE EXCEPTION #======================#
    "SchemaSuperKeyBuildRouteException",
]


# ======================# UNHANDLED_SCHEMA_SUPER_KEY_BUILD_ROUTE EXCEPTION #======================#
class SchemaSuperKeyBuildRouteException(SchemaSuperKeyException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SchemaSuperK build failed because there was no build route for the Schema attribute.

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
    ERROR_CODE = "UNHANDLED_SCHEMA_SUPER_KEY_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SchemaSuperKey build failed: No build path existed for the Schema attribute."