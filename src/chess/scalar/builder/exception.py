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
    # ======================# SCALAR BUILD EXCEPTIONS #======================#
    "ScalarBuildFailedException",
]


# ======================# SCALAR BUILD EXCEPTIONS #======================#
class ScalarBuildFailedException(ScalarException, BuildFailedException):
    """
    Catchall/wrapper exception for when a condition not handled directly by ScalarBuilder 
    prevents successful Scalar creation.
    """
    ERROR_CODE = "SCALAR_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Scalar build failed."
