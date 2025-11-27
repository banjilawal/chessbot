# src/chess/square/builder/exception.py

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
    """
    Catchall exception for when SquareBuilder encounters an error building a new Square instance.
    """
    ERROR_CODE = "SQUARE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Square build failed."

