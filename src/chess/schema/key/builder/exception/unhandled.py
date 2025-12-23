# src/chess/schema/key/builder/exception/unhandled.py

"""
Module: chess.schema.key.builder.exception.unhandled
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.schema import SchemaSuperKeyException


class SchemaSuperKeyBuildUnhandledRouteException(SchemaSuperKeyException, UnhandledRouteException):
    """
    # ROLE: Specialized failure for SchemaSuperKey build unhandled scenarios.
    # RESPONSIBILITIES:
    1. Raised when SchemaSuperKeyBuilder encounters unhandled execution flow during building.
    """
    ERROR_CODE = "SCHEMA_SUPER_KEY_BUILD_UNHANDLED_ROUTE"
    DEFAULT_MESSAGE = (
        "The SchemaSuperKeyBuilder encountered a condition without an appropriate execution route. "
        "Ensure all possible logic branches are covered in the build process."
    )
