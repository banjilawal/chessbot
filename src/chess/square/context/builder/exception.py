# src/chess/square/context/builder/base.py

"""
Module: chess.square.context.builder.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.square import SquareContextException

__all__ = [
    # ======================# SQUARECONTEXT BUILD EXCEPTIONS #======================#
    "SquareContextBuildFailedException",
]


# ======================# SQUARECONTEXT BUILD EXCEPTIONS #======================#
class SquareContextBuildFailedException(SquareContextException, BuildFailedException):
    """
    Catchall/wrapper exception for when a condition not handled directly by SquareContextBuilder 
    prevents successful SquareContext creation.
    """
    ERROR_CODE = "SQUARE_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "SquareContext build failed."