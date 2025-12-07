# src/chess/vector/builder/base.py

"""
Module: chess.vector.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.vector import VectorException
from chess.system import BuildFailedException


__all__ = [
    # ======================# VECTOR BUILD EXCEPTIONS #======================#
    "VectorBuildFailedException",
]


# ======================# VECTOR BUILD EXCEPTIONS #======================#
class VectorBuildFailedException(VectorException, BuildFailedException):
    """
    Catchall/wrapper exception for when a condition not handled directly by VectorBuilder 
    prevents successful Vector creation.
    """
    ERROR_CODE = "VECTOR_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Vector build failed."
