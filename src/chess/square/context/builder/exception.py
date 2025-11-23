# src/chess/square/context/builder/exception.py

"""
Module: chess.square.context.builder.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.square import SquareContextException

__all__ = [
    "SquareContextBuildFailedException",
]


# ======================# SQUARE_CONTEXT BUILD EXCEPTIONS #======================#
class SquareContextBuildFailedException(SquareContextException, BuildFailedException):
    ERROR_CODE = "SQUARE_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "SquareContext build failed."