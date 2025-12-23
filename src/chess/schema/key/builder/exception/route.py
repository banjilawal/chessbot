# src/chess/schema/key/exception.route.py

"""
Module: chess.schema.key.exception.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import InvalidSchemaException, SchemaSuperKeyException
from chess.system import UnhandledRouteException


__all__ = [
    # ======================# UNHANDLED_SCHEMA_SUPER_KEY_BUILD_ROUTE EXCEPTION #======================#
    "SchemaSuperKeyBuildRouteException",
]


# ======================# UNHANDLED_SCHEMA_SUPER_KEY_BUILD_ROUTE EXCEPTION #======================#
class SchemaSuperKeyBuildRouteException(SchemaSuperKeyException, UnhandledRouteException):
    """
    # ROLE: Fallback Result
    
    # RESPONSIBILITIES:
    1. Indicate that Raised when SchemaSuperKeyBuilder encounters unhandled execution flow during a build
    
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
    ERROR_CODE = "UNHANDLED_SCHEMA_SUPER_KEY_BUILD_ROUTE"
    DEFAULT_MESSAGE = (
        "At least one build option or parameter was not handled with its own execution route. Ensure all possible "
        "logic branches are covered in the build process."
    )
