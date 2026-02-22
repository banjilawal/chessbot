# src/chess/board/builder/exception.py

"""
Module: chess.board.builder.exception
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""


from chess.board import BoardException
from chess.system import BuildException

__all__ = [
    # ======================# Board_BUILD_FAILURE #======================#
    "BoardBuildException",
]


# ======================# BOARD_BUILD_FAILURE #======================#
class BoardBuildException(BoardException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Board build creates an exception. Failed check exceptions are encapsulated
        in an BoardBuildException which is sent to the caller in a BuildResult.
    2.  The BoardBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   BoardException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "Board_BUILD_FAILED"
    DEFAULT_MESSAGE = "Board build failed."