# src/chess/system/builder/exception/failure.py

"""
Module: chess.system.builder.exception.failure
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import OperationFailedException

__all__ = [
    # ======================# BUILD_FAILED EXCEPTION #======================#
    "BuildFailedException",
]


# ======================# BUILD_FAILED EXCEPTION #======================#
class BuildFailedException(OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a build operation failed. The encapsulated exceptions create a chain
        for tracing the source of the failure.

    # PARENT:
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BUILD_FAILED"
    DEFAULT_MESSAGE = "build failed."
