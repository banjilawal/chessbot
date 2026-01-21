# src/chess/square/context/builder/exception/wrapper.py

"""
Module: chess.square.context.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.square import SquareContextException


__all__ = [
    # ======================# SQUARE_CONTEXT_BUILD_FAILURE EXCEPTION #======================#
    "SquareContextBuildFailedException",
]


# ======================# SQUARE_CONTEXT_BUILD_FAILURE EXCEPTION #======================#
class SquareContextBuildFailedException(SquareContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the SquareContext build creates an exception. Failed check exceptions are encapsulated
        in an SquareContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The SquareContextBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   SquareContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "SquareContext build failed."