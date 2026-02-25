# src/chess/scalar/builder/.exception.wrapper.py

"""
Module: chess.scalar.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-09-03
version: 1.0.0
"""

from chess.system import BuildException

__all__ = [
    # ======================# SCALAR_BUILD_FAILURE #======================#
    "ScalarBuildException",
]


# ======================# SCALAR_BUILD_FAILURE #======================#
class ScalarBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in ScalarBuilder.build that, prevented BuildResult.success() from 
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
    ERR_CODE = "SCALAR_BUILD_FAILED"
    MSG = "Scalar build failed."