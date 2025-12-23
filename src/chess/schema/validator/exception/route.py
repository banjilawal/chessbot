# src/chess/schema/validator/exception/route.py

"""
Module: chess.schema.validator.exception.route
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
    ERROR_CODE = "UNHANDLED_SCHEMA_VALIDATION_ROUTE"
    DEFAULT_MESSAGE = (
        "The SchemaValidator did not handle a parameter or condition that needs it own execution route. "
        "The validation process was not exhaustive. Ensure all possible branches are covered in the "
        "verification process."
    )