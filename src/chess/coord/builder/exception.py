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
    "CoordBuildFailedException",
]


# ====================== COORD BUILD EXCEPTIONS #======================#
class CoordBuildFailedException(CoordException, BuildFailedException):
    """Catchall exception for when CoordBuilder encounters an error during a Coord build."""
    ERROR_CODE = "COORD_BUILD_FAILED"
    DEFAULT_MESSAGE = "Coord build failed."
