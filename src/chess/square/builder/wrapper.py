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
    # ======================# SQUARE_BUILD_FAILURE #======================#
    "SquareBuildException",
]


# ======================# SQUARE_BUILD_FAILURE #======================#
class SquareBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    An error occurred in SquareBuilder.build that, prevented BuildResult.success() from being returned.

    # PARENT:
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