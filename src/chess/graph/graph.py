# src/chess/graph/graph.py

"""
Module: chess.graph.graph
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from chess.graph import Edge, Node


class Graph:
    """"""
    _id: int
    _edges: List[Edge]
    _vertices: List[Node]

    
    def __init__(self, id: int,):
        self._id = id
        self._edges = []
        self._vertices = []

    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def vertices(self) -> List[Node]:
        return self._vertices
    
    @property
    def edges(self) -> List[Edge]:
        return self._edges