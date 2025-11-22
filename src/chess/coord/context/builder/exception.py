# src/chess/coord/context/builder/exception.py

"""
Module: ches.coord.context.builder.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.coord import CoordContextException


__all__ = [
    "CoordContextBuildFailedException",
]

# ======================# COORD_CONTEXT BUILD EXCEPTIONS #======================#
class CoordContextBuildFailedException(CoordContextException, BuildFailedException):
    """Catchall Exception for CoordContextBuilder when it stops because of an error."""
    ERROR_CODE = "COORD_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "CoordContext build failed."