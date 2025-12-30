# src/chess/schema/key/builder/exception/route.py

"""
Module: chess.schema.key.builder.exception.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ResultException, UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_SCHEMA_SUPER_KEY_BUILD_ROUTE EXCEPTION #======================#
    "SchemaSuperKeyBuildRouteException",
]


# ======================# UNHANDLED_SCHEMA_SUPER_KEY_BUILD_ROUTE EXCEPTION #======================#
class SchemaSuperKeyBuildRouteException(ResultException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that SchemaSuperKeyBuilder did not handle one of the paths necessary to assure a candidate is a
        safe to use SchemaSuperKey. There are different configurations of SchemaSuperKey that are correct. Each
        configuration must have a build route to guarantee all SchemaSuperKey products are safe. If a
        SchemaSuperKey configuration does not have a build route the last step in the logic will return a
        BuildResult containing a SchemaSuperKeyBuildRouteException.

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
    ERROR_CODE = "UNHANDLED_SCHEMA_SUPER_KEY_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "The SchemaSuperKeyBuilder did not handle one of the paths necessary to guarantee SchemaSuperKeys are "
        "safe products. Ensure all possible build branches are covered to ensure the execution flow does not "
        "hit the default failure result outside the if-blocks."
    )