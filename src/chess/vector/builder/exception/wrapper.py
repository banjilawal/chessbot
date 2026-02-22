# src/chess/vector/builder/exception/wrapper.py

"""
Module: chess.vector.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.vector import VectorException
from chess.system import BuildException

__all__ = [
    # ======================# VECTOR_BUILD_FAILURE #======================#
    "VectorBuildException",
]


# ======================# VECTOR_BUILD_FAILURE #======================#
class VectorBuildException(VectorException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Vector build creates an exception. Failed check exceptions are encapsulated
        in an VectorBuildException which is sent to the caller in a BuildResult.
    2.  The VectorBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   VectorException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "VECTOR_BUILD_FAILED"
    DEFAULT_MESSAGE = "Vector build failed."