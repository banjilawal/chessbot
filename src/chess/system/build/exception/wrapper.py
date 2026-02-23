# src/chess/system/builder/exception/wrapper.py

"""
Module: chess.system.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import OperationException

__all__ = [
    # ======================# BUILD_FAILURE #======================#
    "BuildException",
]


# ======================# BUILD_FAILURE #======================#
class BuildException(OperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes what condition prevented the build 
        from completing.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BUILD_FAILURE"
    DEFAULT_MESSAGE = "Build failed."
