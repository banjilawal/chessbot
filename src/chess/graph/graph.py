# src/chess/graph/graph.py

"""
Module: chess.graph.graph
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from chess.graph import Vertex


class Graph:
    """"""
    _id: int
    _vertices: List[Vertex]
    _edges: List[Edge]
    
    def __init__(
            self,
            id: int,
    ):
        self._id = id
        self._vertices = List[Vertex]
        self._edges = List[Edge]
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def vertices(self) -> List[Vertex]:
        return self._vertices
    
    @property
    def edges(self) -> List[Edge]:
        return self._edges