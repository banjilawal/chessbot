# src/chess/system/build/result/exception/empty.py

"""
Module: chess.system.build.result.exception.empty
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BuildException, ResultException


__all__ = [
    # ======================# EMPTY_BUILD_RESULT EXCEPTION #======================#
    "EmptyBuildResultException",
]


# ======================# EMPTY_BUILD_RESULT EXCEPTION #======================#
class EmptyBuildResultException(BuildException, ResultException):
    """
    # ROLE: Messanger  Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Indicate that a Build result contains neither a payload nor an exception.

    # PARENT:
        *   BuildException
        *   ResultException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EMPTY_BUILD_RESULT_ERROR"
    DEFAULT_MESSAGE = "BuildResult must contain either a payload or an exception. It cannot be empty."