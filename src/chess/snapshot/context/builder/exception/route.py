# src/chess/snapshot/context/builder/exception/route.py

"""
Module: chess.snapshot.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_SNAPSHOT_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "SnapshotContextBuildRouteException",
]

from chess.snapshot import SnapshotContextException
from chess.system import ExecutionRouteException


# ======================# NO_SNAPSHOT_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class SnapshotContextBuildRouteException(SnapshotContextException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SnapshotContext build failed because there was no build route for the Snapshot key.

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
    ERR_CODE = "NO_SNAPSHOT_CONTEXT_BUILD_ROUTE_EXCEPTION"
    MSG = "SnapshotContext build failed: No build path existed for the Snapshot key."