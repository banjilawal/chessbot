# src/chess/square/builder/exception/wrapper.py

"""
Module: chess.square.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-09-02
version: 1.0.0
"""

from  chess.square import SquareException
from chess.system import BuildException

__all__ = [
    # ======================# SQUARE_BUILD_FAILURE #======================#
    "SquareBuildException",
]


# ======================# SQUARE_BUILD_FAILURE #======================#
class SquareBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in SquareBuilder.build that, prevented BuildResult.success() from
        being returned.

    # PARENT:
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_BUILD_FAILED"
    MSG = "Square build failed."