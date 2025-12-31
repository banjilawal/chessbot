# src/chess/schema/key/validator/exception/debug/route.py

"""
Module: chess.schema.key.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaSuperKey
from chess.system import UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_SCHEMA_SUPER_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "SchemaSuperKeyValidationRouteException",
]


# ======================# UNHANDLED_SCHEMA_SUPER_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class SchemaSuperKeyValidationRouteException(SchemaSuperKey, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate failed SchemaSuperKey validation because no validation route for its attribute.

    # PARENT:
        *   SchemaSuperKey
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SCHEMA_SUPER_KEY_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SchemaSuperKey validation failed: No validation route was provided for the Schema attribute."