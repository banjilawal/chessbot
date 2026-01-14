# src/chess/snapshot/context/builder/exception/route.py

"""
Module: chess.snapshot.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_SNAPSHOT_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "SnapshotContextBuildRouteException",
]

from chess.snapshot import SnapshotContextException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_SNAPSHOT_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class SnapshotContextBuildRouteException(SnapshotContextException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SnapshotContext build failed because there was no build route for the Snapshot key.

    # PARENT:
        *   SnapshotContextException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SNAPSHOT_CONTEXT_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SnapshotContext build failed: No build path existed for the Snapshot key."