# src/chess/node/context/validator/exception/debug/null/node.py

"""
Module: chess.node.context.validator.exception.debug.null.node
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_NODE EXCEPTION #======================#
    "NullNodeException",
]

from chess.system import NullException
from chess.node import NodeDebugException


# ======================# NULL_NODE EXCEPTION #======================#
class NullNodeException(NodeDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the validation candidate was null.

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
    ERROR_CODE = "NULL_NODE_ERROR"
    DEFAULT_MESSAGE = "Node validation failed: The validation candidate cannot be null."