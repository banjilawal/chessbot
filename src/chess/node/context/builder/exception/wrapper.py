# src/chess/node/context/builder/exception/wrapper.py

"""
Module: chess.node.context.builder.exception.wrapper
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.node import NodeContextException


__all__ = [
    # ======================# NODE_CONTEXT_BUILD_FAILURE EXCEPTION #======================#
    "NodeContextBuildFailedException",
]


# ======================# NODE_CONTEXT_BUILD_FAILURE EXCEPTION #======================#
class NodeContextBuildFailedException(NodeContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the NodeContext build creates an exception. Failed check exceptions are encapsulated
        in an NodeContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The NodeContextBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   NodeContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "NodeContext build failed."