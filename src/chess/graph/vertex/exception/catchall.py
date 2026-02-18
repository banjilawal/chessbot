# src/chess/graph/node/exception/catchall.py

"""
Module: chess.graph.node.exception.catchall
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# NODE EXCEPTION #======================#
    "NodeException",
]

class NodeException(ChessException):
    pass