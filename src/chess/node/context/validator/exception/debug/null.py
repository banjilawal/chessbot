# src/chess/node/context/validator/exception/debug/null.py

"""
Module: chess.node.context.validator.exception.debug.null
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.system import NullException
from chess.node import NodeContextException

__all__ = [
    # ======================# NULL_NODE_CONTEXT EXCEPTION #======================#
    "NullNodeContextException",
]


# ======================# NULL_NODE_CONTEXT EXCEPTION #======================#
class NullNodeContextException(NodeContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its validation as a NodeContext because it was null.

    # PARENT:
        *   NodeContextException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_NODE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "NodeContext validation failed: The candidate was null."