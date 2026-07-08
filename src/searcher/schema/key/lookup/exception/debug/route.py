# src/logic/schema/key/lookup/exception/debug/route.py

"""
Module: logic.schema.key.lookup.exception.debug.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from model.catalog import SchemaException
from system import ExecutionRouteException


__all__ = [
    # ======================# NO_SCHEMA_LOOKUP_ROUTE EXCEPTION #======================#
    "SchemaLookupRouteException",
]


# ======================# NO_SCHEMA_LOOKUP_ROUTE EXCEPTION #======================#
class SchemaLookupRouteException(SchemaException, ExecutionRouteException):
    """
    Role:Fallback Result
    
    Responsibilities:
    1. Indicate that SchemaLookupProcess did not handle a build option or parameter with its own execution route.
    
    Super Class:
        *   SchemaException
        *   ExecutionRouteException

        
    # PROVIDES
    None
    
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_SCHEMA_LOOKUP_ROUTE_EXCEPTION"
    MSG = "SchemaLookupProcess failed: No search route was provided for a Schema attribute."
 