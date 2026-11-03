# src/graph/graph.py

"""
Module: graph.graph
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from collection import EdgeStackService, VertexStackService


class Graph:
    _edges: EdgeStackService
    _vertices: VertexStackService
    
    def __init__(
            self,
            edges: Optional[EdgeStackService] | None = None,
            vertices: Optional[VertexStackService] | None = None,
    ):
        self._edges = edges or EdgeStackService()
        self._vertices = vertices or VertexStackService()
        
    @property
    def edges(self) -> EdgeStackService:
        return self._edges
        
    @property
    def vertices(self) -> VertexStackService:
        return self._vertices
        