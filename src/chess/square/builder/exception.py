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
    # ======================# SQUARE_BUILD_FAILED EXCEPTION #======================#
    "SquareBuildFailedException",
]


# ======================# SQUARE_BUILD_FAILED EXCEPTION #======================#
class SquareBuildFailedException(SquareException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Square build creates an exception. Failed check exceptions are encapsulated
        in an SquareBuildFailedException which is sent to the caller in a BuildResult.
    2.  The SquareBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   SquareException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_BUILD_FAILED"
    DEFAULT_MESSAGE = "Square build failed."