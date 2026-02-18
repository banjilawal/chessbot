# src/chess/node/validator/exception/debug/null.py

"""
Module: chess.node.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from chess.graph import NodeException
from chess.system import NullException

__all__ = [
    # ======================# NULL_NODE EXCEPTION #======================#
    "NullNodeException",
]

class NullNodeException(NodeException, NullException):
    pass