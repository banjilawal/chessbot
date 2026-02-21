# src/chess/square/builder/exception.py

"""
Module: chess.square.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from  chess.square import SquareException
from chess.system import BuildException

__all__ = [
    # ======================# SQUARE_BUILD_FAILURE EXCEPTION #======================#
    "SquareBuildException",
]


# ======================# SQUARE_BUILD_FAILURE EXCEPTION #======================#
class SquareBuildException(SquareException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Square build creates an exception. Failed check exceptions are encapsulated
        in an SquareBuildException which is sent to the caller in a BuildResult.
    2.  The SquareBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   SquareException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_BUILD_FAILED"
    DEFAULT_MESSAGE = "Square build failed."