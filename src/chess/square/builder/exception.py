# src/chess/square/builder/collision.py

"""
Module: chess.square.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from  chess.square import SquareException
from chess.system import BuildFailedException

__all__ = [
    # ======================# SQUARE BUILD EXCEPTIONS #======================#
    "SquareBuildFailedException",
]

# ======================# SQUARE BUILD EXCEPTIONS #======================#
class SquareBuildFailedException(SquareException, BuildFailedException):
    """Catchall Exception for SquareBuilder when it encounters an error building a Square."""
    ERROR_CODE = "SQUARE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Square build failed."

