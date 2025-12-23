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
    # ROLE: Fallback Result
    
    # RESPONSIBILITIES:
    1. Indicate that SchemaSuperKeyBuilder did not handle a build option or parameter with its own execution route.
    
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
