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
    # ======================# SCALAR_BUILD_FAILURE EXCEPTION #======================#
    "ScalarBuildFailedException",
]


# ======================# SCALAR_BUILD_FAILURE EXCEPTION #======================#
class ScalarBuildFailedException(ScalarException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Scalar build creates an exception. Failed check exceptions are encapsulated
        in an ScalarBuildFailedException which is sent to the caller in a BuildResult.
    2.  The ScalarBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   ScalarException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCALAR_BUILD_FAILED"
    DEFAULT_MESSAGE = "Scalar build failed."