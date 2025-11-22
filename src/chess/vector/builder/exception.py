# src/chess/vector/builder/exception.py

"""
Module: chess.vector.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.vector import VectorException
from chess.system import BuildFailedException

__all__ = ("VectorBuildFailedException",)


# ======================# VECTOR BUILD EXCEPTIONS #======================#
class VectorBuildFailedException(VectorException, BuildFailedException):
    """Catchall Exception for VectorBuilder when it encounters an error building a Vector."""
    ERROR_CODE = "VECTOR_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Vector build failed."
