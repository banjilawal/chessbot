# src/chess/graph/edge/vertex.py

"""
Module: chess.graph.edge.vertex
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from __future__ import annotations

from chess.graph import Vertex


class Edge:
    _id: int
    _head: Vertex
    _tail: Vertex
    _distance: int
    _heuristic: int
    _weight: int
    
    
    