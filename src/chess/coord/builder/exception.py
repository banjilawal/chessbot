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
    # ======================# COORD BUILD EXCEPTIONS #======================#
    "CoordBuildFailedException",
]


# ======================# COORD BUILD EXCEPTIONS #======================#
class CoordBuildFailedException(CoordException, BuildFailedException):
    """
    Catchall/wrapper exception for when a condition not handled directly by CoordBuilder 
    prevents successful Coord creation.
    """
    ERROR_CODE = "COORD_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Coord build failed."
