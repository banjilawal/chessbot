# src/logic/node/context/validator/exception/debug/null/node.py

"""
Module: logic.node.context.validator.exception.debug.null.node
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_NODE EXCEPTION #======================#
    "NullNodeException",
]

from logic.system import NullException
from logic.node import NodeDebugException


# ======================# NULL_NODE EXCEPTION #======================#
class NullNodeException(NodeDebugException, NullException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the candidate was null.

    # PARENT:
        *   NodeDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_NODE_EXCEPTION"
    MSG = "Node validation failed: The candidate cannot be null."