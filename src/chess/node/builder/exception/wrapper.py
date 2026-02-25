# src/chess/node/builder/exception/wrapper.py

"""
Module: chess.node.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BuildException

__all__ = [
    # ======================# NODE_BUILD_FAILURE #======================#
    "NodeBuildException",
]


# ======================# NODE_BUILD_FAILURE #======================#
class NodeBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in NodeBuilder.build that, prevented BuildResult.success() from 
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
    ERR_CODE = "NODE_BUILD_FAILED"
    MSG = "Node build failed."