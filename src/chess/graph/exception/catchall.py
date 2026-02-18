# src/chess/graph/exception/catchall.py

"""
Module: chess.graph.exception.catchall
Author: Banji Lawal
Created: 2025-02-18
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# GRAPH EXCEPTION #======================#
    "GraphException",
]

class GraphException(ChessException):
    pass