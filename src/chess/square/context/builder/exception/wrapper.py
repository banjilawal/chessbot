# src/chess/square/context/builder/exception/wrapper.py

"""
Module: chess.square.context.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import BuildException
from chess.square import SquareContextException


__all__ = [
    # ======================# SQUARE_CONTEXT_BUILD_FAILURE #======================#
    "SquareContextBuildException",
]


# ======================# SQUARE_CONTEXT_BUILD_FAILURE #======================#
class SquareContextBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    An error occurred in SquareContextBuilder.build that, prevented BuildResult.success()
    from being returned.

    # PARENT:
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "SquareContext build failed."