# src/chess/schema/key/validator/exception/debug/route.py

"""
Module: chess.schema.key.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_SCHEMA_SUPER_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "SchemaSuperKeyValidationRouteException",
]

from chess.schema import SchemaSuperKeyException
from chess.system import UnhandledRouteException


# ======================# UNHANDLED_SCHEMA_SUPER_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class SchemaSuperKeyValidationRouteException(SchemaSuperKeyException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that SchemaSuperKeyValidator did not handle one of the paths necessary to assure a candidate is a
        safe to use SchemaSuperKey. There are different configurations of SchemaSuperKey that are correct. Each
        configuration must have a testing route for a thorough verification process. If a SchemaSuperKey configuration
        does not have a validation route the last step in the logic will return a ValidationResult containing a
        SchemaSuperKeyValidationRouteException.

    # PARENT:
        *   ResultException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SCHEMA_SUPER_KEY_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The SchemaSuperKeyValidator did not handle one of the paths necessary to assure a candidate is a safe to use"
        "SchemaSuperKey. Ensure all possible verification branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-verification-blocks."
    )