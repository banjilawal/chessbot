# src/chess/vector/builder/exception/wrapper.py

"""
Module: chess.vector.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.vector import VectorException
from chess.system import BuildFailedException

__all__ = [
    # ======================# VECTOR_BUILD_FAILED EXCEPTION #======================#
    "VectorBuildFailedException",
]


# ======================# VECTOR_BUILD_FAILED EXCEPTION #======================#
class VectorBuildFailedException(VectorException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Vector build creates an exception. Failed check exceptions are encapsulated
        in an VectorBuildFailedException which is sent to the caller in a BuildResult.
    2.  The VectorBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   VectorException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VECTOR_BUILD_FAILED"
    DEFAULT_MESSAGE = "Vector build failed."