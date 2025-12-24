# src/chess/board/builder/exception.py

"""
Module: chess.board.builder.exception
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""


from chess.board import BoardException
from chess.system import BuildFailedException

__all__ = [
    # ======================# Board_BUILD_FAILED EXCEPTION #======================#
    "BoardBuildFailedException",
]


# ======================# BOARD_BUILD_FAILED EXCEPTION #======================#
class BoardBuildFailedException(BoardException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Board build creates an exception. Failed check exceptions are encapsulated
        in an BoardBuildFailedException which is sent to the caller in a BuildResult.
    2.  The BoardBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   BoardException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "Board_BUILD_FAILED"
    DEFAULT_MESSAGE = "Board build failed."