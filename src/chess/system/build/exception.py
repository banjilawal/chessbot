# src/chess/system/builder/exception/failure.py

"""
Module: chess.system.builder.exception.failure
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# BUILD_FAILED EXCEPTION #======================#
    "BuildFailedException",
]


# ======================# BUILD_FAILED EXCEPTION #======================#
class BuildFailedException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an exception prevented a build operation from completing successfully.
    2.  Wrap an exception that hits the try-finally block of a Build method.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BUILD_FAILED"
    DEFAULT_MESSAGE = "build failed. An exception prevented the build from completing."
