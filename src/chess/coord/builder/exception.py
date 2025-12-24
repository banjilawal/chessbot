# src/chess/coord/builder/collision.py

"""
Module: chess.coord.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.coord import CoordException
from chess.system import BuildFailedException

__all__ = [
    # ======================# COORD_BUILD_FAILED EXCEPTION #======================#
    "CoordBuildFailedException",
]


# ======================# COORD_BUILD_FAILED EXCEPTION #======================#
class CoordBuildFailedException(CoordException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Coord build creates an exception. Failed check exceptions are encapsulated
        in an CoordBuildFailedException which is sent to the caller in a BuildResult.
    2.  The CoordBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   CoordException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_BUILD_FAILED"
    DEFAULT_MESSAGE = "Coord build failed."