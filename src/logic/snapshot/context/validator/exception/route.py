# src/logic/snapshot/context/validator/exception/debug/route.py

"""
Module: logic.snapshot.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "SnapshotContextValidationRouteException",
]

from logic.snapshot import SnapshotContextException
from logic.system import ExecutionRouteException


# ======================# NO_SNAPSHOT_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class SnapshotContextValidationRouteException(SnapshotContextException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SnapshotContext validation failed because there was no build route for the SnapshotContext key.

    # PARENT:
        *   SnapshotContextException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_SNAPSHOT_CONTEXT_VALIDATION_ROUTE_EXCEPTION"
    MSG = "SnapshotContext validation failed: No validation route was provided for the Snapshot attribute."