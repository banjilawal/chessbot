# src/chess/graph/vertex/vertex.py

"""
Module: chess.graph.vertex.vertex
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from __future__ import annotations

from typing import List

from chess.square import Square
from chess.graph import DiscoveryStatus, Edge


class Vertex:
    _priority: int
    _square: Square
    _predecessor: Vertex
    _incoming_edges: List[Edge]
    _outgoing_edges: List[Edge]
    _discovery_status: DiscoveryStatus
    