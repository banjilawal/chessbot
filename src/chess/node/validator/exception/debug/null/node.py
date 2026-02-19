# src/chess/node/validator/exception/debug/null.py

"""
Module: chess.node.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_NODE EXCEPTION #======================#
    "NullNodeException",
]

from chess.system import NullException
from chess.node import NodeException


# ======================# NULL_NODE EXCEPTION #======================#
class NullNodeException(NodeException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that an entity, method, or operation that required a Node but got null instead.

    # PARENT:
        *   NullNodeException
        *   NodeValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_NODE_ERROR"
    DEFAULT_MESSAGE = "Node cannot be null."