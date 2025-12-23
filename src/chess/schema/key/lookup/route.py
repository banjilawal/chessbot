# src/chess/schema/key/lookup/route.py

"""
Module: chess.schema.key.lookup.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from chess.schema.lookup.forward.wrapper import ForwardSchemaFailedException
from chess.system import UnhandledRouteException


__all__ = [
    # ======================# UNHANDLED_FORWARD_SCHEMA_LOOKUP_ROUTE EXCEPTION #======================#
    "ForwardSchemaRouteException",
]


# ======================# UNHANDLED_FORWARD_SCHEMA_LOOKUP_ROUTE EXCEPTION #======================#
class ForwardSchemaRouteException(ForwardSchemaFailedException, UnhandledRouteException):
    """
    # ROLE: Fallback Result
    
    # RESPONSIBILITIES:
    1. Indicate that ForwardSchemaLookuper did not handle a build option or parameter with its own execution route.
    
    # PARENT:
        *   UnhandledRouteException
        *   ForwardSchemaLookupFailedException
        
    # PROVIDES
    None
    
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_FORWARD_SCHEMA_LOOKUP_ROUTE"
    DEFAULT_MESSAGE = (
        "The ForwardSchemaLookup did not handle a parameter or condition that needs it own execution route. "
        "The build process was not exhaustive. Conditions necessary for ForwardSchemaLookup integrity were skipped. "
        "Ensure all possible branches are covered in the verification process."
    )
 