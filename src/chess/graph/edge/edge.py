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
    
    
    def __init__(self, id: int, head: Vertex, tail: Vertex, distance: int, heuristic: int):
        self._id = id
        self._head = head
        self._tail = tail
        self._distance = distance
        self._heuristic = heuristic
        self._weight = distance + heuristic
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def head(self) -> Vertex:
        return self._head
    
    @property
    def tail(self):
        return self._tail
    
    @property
    def distance(self) -> int:
        return self._distance
    
    @property
    def heuristic(self) -> int:
        return self._heuristic
    
    @property
    def weight(self) -> int:
        return self._weight
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Edge): return self._id == other._id
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    
    