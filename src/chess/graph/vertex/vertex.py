# src/chess/graph/square/vertex.py

"""
Module: chess.graph.square.vertex
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from chess.square import Square


class Vertex:
    _priority: int
    _square: Square
    _predecessor: Vertex
    _incoming_edges: List[Edge]
    _outgoing_edges: List[Edge]
    _discovery_status: DiscoveryStatus
    