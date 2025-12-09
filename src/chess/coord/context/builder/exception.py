# src/chess/coordContext/context/builder/exception.py

"""
Module: ches.coordContext.context.builder.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.coord import CoordContextException

__all__ = [
    #======================# COORDCONTEXT BUILD EXCEPTIONS #======================#
    "CoordContextBuildFailedException",
]


#======================# COORDCONTEXT BUILD EXCEPTIONS #======================#
class CoordContextBuildFailedException(CoordContextException, BuildFailedException):
    """
    Catchall/wrapper exception for when a condition not handled directly by CoordContextBuilder 
    prevents successful CoordContext creation.
    """
    ERROR_CODE = "COORD_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "CoordContext build failed."