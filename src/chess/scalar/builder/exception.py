# src/chess/scalar/builder/exception.py

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
    """Catchall Exception for ScalarBuilder when it encounters an error building a Scalar."""
    ERROR_CODE = "SCALAR_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Scalar build failed."
