# src/chess/node/context/validator/exception/debug/excess.py

"""
Module: chess.node.context.validator.exception.debug.excess
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.node import NodeContextException

__all__ = [
    # ========================= EXCESSIVE_NODE_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveNodeContextFlagsException"
]


# ========================= EXCESSIVE_NODE_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveNodeContextFlagsException(NodeContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its validation as a NodeContext because more than one of its attributes
        was enabled.

    # PARENT:
        *   ContextFlagCountException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_NODE_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "NodeContext validation failed: More than one flag was enable."