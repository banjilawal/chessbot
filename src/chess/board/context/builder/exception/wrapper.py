# src/chess/board/context/builder/exception/wrapper.py

"""
Module: chess.board.context.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.board import BoardContextException

__all__ = [
    # ======================# BOARD_CONTEXT_BUILD_FAILED EXCEPTION #======================#
    "BoardContextBuildFailedException",
]


# ======================# BOARD_CONTEXT_BUILD_FAILED EXCEPTION #======================#
class BoardContextBuildFailedException(BoardContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the BoardContext build creates an exception. Failed check exceptions are encapsulated
        in an BoardContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The BoardContextBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   BoardContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "BoardContext build failed."