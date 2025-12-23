# src/chess/schema/key/exception.route.py

"""
Module: chess.schema.key.exception.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaSuperKeyException
from chess.system import UnhandledRouteException


class SchemaSuperKeyBuildUnhandledRouteException(SchemaSuperKeyException, UnhandledRouteException):
    """
    # ROLE: Specialized failure for SchemaSuperKey build unhandled scenarios.
    
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
    ERROR_CODE = "SCHEMA_SUPER_KEY_BUILD_UNHANDLED_ROUTE"
    DEFAULT_MESSAGE = (
        "The SchemaSuperKeyBuilder encountered a condition without an appropriate execution route. "
        "Ensure all possible logic branches are covered in the build process."
    )
