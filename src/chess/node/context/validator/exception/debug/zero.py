# src/chess/node/context/validator/exception/debug/zero.py

"""
Module: chess.node.context.validator.exception.debug.zero
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.node import NodeContextException

__all__ = [
    # ========================= ZERO_NODE_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroNodeContextFlagsException"
]


# ========================= ZERO_NODE_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroNodeContextFlagsException(NodeContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its validation as a NodeContext because none of its attributes was enabled.
        A single NodeContext attribute.

    # PARENT:
        *   ContextFlagCountException
        *   NodeContextValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_NODE_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "NodeContext validation failed: None of the flags were set. A single flag must be enabled."