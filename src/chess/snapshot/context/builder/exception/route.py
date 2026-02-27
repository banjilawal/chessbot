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
from chess.system import NoExecutionRouteException


# ======================# NO_SNAPSHOT_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class SnapshotContextBuildRouteException(SnapshotContextException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SnapshotContext build failed because there was no build route for the Snapshot key.

    # PARENT:
        *   SnapshotContextException
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_SNAPSHOT_CONTEXT_BUILD_ROUTE_EXCEPTION"
    MSG = "SnapshotContext build failed: No build path existed for the Snapshot key."