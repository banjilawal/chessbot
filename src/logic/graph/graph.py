# src/logic/graph/graph.py

"""
Module: logic.graph.graph
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from __future__ import annotations

from logic.edge import EdgeStack
from logic.node import NodeStackService


class Graph:
    """"""
    _id: int
    _edges: EdgeStack
    _vertices: NodeStackService
    
    def __init__(self, id: int):
        self._id = id
        self._edges = EdgeStack()
        self._vertices = NodeStackService()
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def edges(self) -> EdgeStack:
        return self._edges
    
    @property
    def vertices(self) -> NodeStackService:
        return self._vertices
    
