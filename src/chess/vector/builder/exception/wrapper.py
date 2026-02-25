# src/chess/vector/builder/exception/wrapper.py

"""
Module: chess.vector.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BuildException

__all__ = [
    # ======================# VECTOR_BUILD_FAILURE #======================#
    "VectorBuildException",
]


# ======================# VECTOR_BUILD_FAILURE #======================#
class VectorBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in VectorBuilder.build that, prevented BuildResult.success() from 
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
    ERR_CODE = "VECTOR_BUILD_FAILED"
    MSG = "Vector build failed."