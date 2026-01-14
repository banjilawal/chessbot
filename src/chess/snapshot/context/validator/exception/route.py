# src/chess/snapshot/context/validator/exception/debug/route.py

"""
Module: chess.snapshot.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "SnapshotContextValidationRouteException",
]

from chess.snapshot import SnapshotContextException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_SNAPSHOT_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class SnapshotContextValidationRouteException(SnapshotContextException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SnapshotContext validation failed because there was no build route for the SnapshotContext key.

    # PARENT:
        *   SnapshotContextException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SNAPSHOT_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SnapshotContext validation failed: No validation route was provided for the Snapshot attribute."