# src/chess/schema/key/lookup/exception/debug/route.py

"""
Module: chess.schema.key.lookup.exception.debug.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaException
from chess.system import UnhandledRouteException


__all__ = [
    # ======================# UNHANDLED_SCHEMA_LOOKUP_ROUTE EXCEPTION #======================#
    "SchemaLookupRouteException",
]


# ======================# UNHANDLED_SCHEMA_LOOKUP_ROUTE EXCEPTION #======================#
class SchemaLookupRouteException(SchemaException, UnhandledRouteException):
    """
    # ROLE: Fallback Result
    
    # RESPONSIBILITIES:
    1. Indicate that SchemaLookup did not handle a build option or parameter with its own execution route.
    
    # PARENT:
        *   SchemaException
        *   UnhandledRouteException

        
    # PROVIDES
    None
    
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SCHEMA_LOOKUP_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SchemaLookup failed: No search route was provided for a Schema attribute."
 