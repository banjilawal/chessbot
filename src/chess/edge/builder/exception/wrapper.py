# src/chess/edge/builder/wrapper.py

"""
Module: chess.edge.builder.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildException

__all__ = [
    # ======================# EDGE_BUILD_FAILURE #======================#
    "EdgeBuildException",
]


# ======================# EDGE_BUILD_FAILURE #======================#
class EdgeBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in EdgeBuilder.build that, prevented BuildResult.success() from
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
    ERR_CODE = "EDGE_BUILD_FAILED"
    MSG = "Edge build failed."