# src/chess/schema/key/exception.route.py

"""
Module: chess.schema.key.exception.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import InvalidSchemaException
from chess.system import UnhandledRouteException


__all__ = [
    # ======================# UNHANDLED_SCHEMA_VALIDATION_ROUTE EXCEPTION #======================#
    "UnhandledSchemValidationRouteException",
]


# ======================# UNHANDLED_SCHEMA_VALIDATION_ROUTE EXCEPTION #======================#
class UnhandledSchemValidationRouteException(InvalidSchemaException, UnhandledRouteException):
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
    ERROR_CODE = "UNHANDLED_SCHEMA_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The SchemaBuilder encountered a condition without an appropriate execution route. "
        "Ensure all possible logic branches are covered in the build process."
    )
