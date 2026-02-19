# src/chess/node/exception/catchall.py

"""
Module: chess.node.exception.catchall
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

__all__ = [
    # ======================# NODE EXCEPTION #======================#
    "NodeException",
]

from chess.system import ChessException


# ======================# NODE EXCEPTION #======================#
class NodeException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Node errors not covered by NodeException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NODE_ERROR"
    DEFAULT_MESSAGE = "Node raised an exception."