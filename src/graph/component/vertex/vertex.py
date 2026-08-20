# src/graph/component/vertex/vertex.py

"""
Module: graph.component.vertex.vertex
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from model import Dossier
from node import DiscoveryStatus
from collection.stack import EdgeStackService


class Vertex:
    _square_dossier: Dossier
    _priority: Optional[int]
    _predecessor:Optional[Vertex]
    _incoming_edges: EdgeStackService
    _outgoing_edges: EdgeStackService
    _discovery_status: DiscoveryStatus
    
    
    def __init__(
            self,
            square_dossier: square_dossier,
            incoming_edges: Optional[EdgeStackService]| None = None,
            outgoing_edges: Optional[EdgeStackService] | None = None,
    ):
        self._square_dossier = square_dossier
        self._incoming_edges = incoming_edges or EdgeStackService()
        self._outgoing_edges = outgoing_edges or EdgeStackService()
        
        self._priority = None
        self._predecessor = None
        self._discovery_status = DiscoveryStatus.UNKNOWN
    
    @property
    def square_dossier(self) -> Dossier:
        return self._square_dossier
    
    @property
    def incoming_edges(self) -> EdgeStackService:
        return self._incoming_edges
    
    @property
    def outgoing_edges(self) -> EdgeStackService:
        return self._outgoing_edges
    
    @property
    def discovery_status(self) -> DiscoveryStatus:
        return self._discovery_status
    
    @discovery_status.setter
    def discovery_status(self, status: DiscoveryStatus):
        self._discovery_status = status
        
    @property
    def priority(self) -> Optional[int]:
        return self._priority
    
    @priority.setter
    def priority(self, priority: int):
        self._priority = priority
        
    @property
    def predecessor(self) -> Optional[Vertex[T]]:
        return self._predecessor
    
    @predecessor.setter
    def predecessor(self, predecessor: Vertex[T]):
        self._predecessor = predecessor
        
    