# src/chess/coord/builder/collision.py

"""
Module: chess.coord.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.coord import CoordException
from chess.system import BuildException

__all__ = [
    # ======================# COORD_BUILD_FAILURE #======================#
    "CoordBuildException",
]


# ======================# COORD_BUILD_FAILURE #======================#
class CoordBuildException(CoordException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Coord build creates an exception. Failed check exceptions are encapsulated
        in an CoordBuildException which is sent to the caller in a BuildResult.
    2.  The CoordBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   CoordException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_BUILD_FAILED"
    DEFAULT_MESSAGE = "Coord build failed."