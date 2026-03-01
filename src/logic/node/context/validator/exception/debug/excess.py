# src/logic/node/context/validator/exception/debug/excess.py

"""
Module: logic.node.context.validator.exception.debug.excess
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from logic.system import ContextFlagCountException
from logic.node import NodeContextException

__all__ = [
    # ========================= ARENA_NODE_CONTEXT_FLAG EXCEPTION =========================#
    "ArenaNodeContextFlagsException"
]


# ========================= ARENA_NODE_CONTEXT_FLAG EXCEPTION =========================#
class ArenaNodeContextFlagsException(NodeContextException, ContextFlagCountException):
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
    ERR_CODE = "ARENA_NODE_CONTEXT_FLAG_EXCEPTION"
    MSG = "NodeContext validation failed: More than one flag was enable."