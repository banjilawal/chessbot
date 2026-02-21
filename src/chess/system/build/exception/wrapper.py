# src/chess/system/builder/exception/wrapper.py

"""
Module: chess.system.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import OperationFailedException

__all__ = [
    # ======================# BUILD_FAILURE #======================#
    "BuildException",
]


# ======================# BUILD_FAILURE #======================#
class BuildException(OperationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a build operation failed. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BUILD_FAILURE"
    DEFAULT_MESSAGE = "build failed."
