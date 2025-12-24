# src/board/searcher/exception.py

"""
Module: chess.board.searcher.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""
from chess.board.context import BoardContextException
from chess.system import (
    BuildOptionSelectionTooLargeException, ContextException, NoBuildOptionSelectedException, NullException,
    BuildFailedException, ValidationException,
)

___all__ = [
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
    ERROR_CODE = "BOARD_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "BoardContext build failed."