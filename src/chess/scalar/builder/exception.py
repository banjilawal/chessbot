# src/chess/scalar/builder/collision.py

"""
Module: chess.scalar.builder.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.scalar import ScalarException
from chess.system import BuildFailedException

__all__ = [
    "ScalarBuildFailedException",
]

# ======================# SCALAR BUILD EXCEPTIONS #======================#
class ScalarBuildFailedException(ScalarException, BuildFailedException):
    """
    Catchall exception for when ScalarBuilder encounters an error building a new Scalar instance.
    """
    ERROR_CODE = "SCALAR_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Scalar build failed."
