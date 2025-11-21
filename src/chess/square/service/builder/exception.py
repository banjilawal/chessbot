# src/chess/square/service/builder/exception.py

"""
Module: chess.square.service.builder.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.square import SquareServiceException

__all__ = [
    "SquareServiceBuildFailedException",
]

# ======================# SQUARE_SERVICE BUILD EXCEPTIONS #======================#
class SquareServiceBuildFailedException(SquareServiceException, BuildFailedException):
    """Catchall Exception for SquareServiceBuilder when it encounters an error building a Square."""
    ERROR_CODE = "SQUARE_SERVICE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "SquareService build failed."
