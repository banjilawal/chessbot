# src/node/model/state.py

"""
Module: node.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from model import Element, StateModel
from node import DiscoveryStatus
from stack import EdgeStackService

T = TypeVar("T")

class Node(StateModel, Generic[T]):
    _element: Element
    _priority: Optional[int]
    _predecessor:Optional[Node[T]]
    _incoming_edges: EdgeStackService
    _outgoing_edges: EdgeStackService
    _discovery_status: DiscoveryStatus
    
    
    def __init__(
            self,
            element: element,
            incoming_edges: Optional[EdgeStackService]| None = None,
            outgoing_edges: Optional[EdgeStackService] | None = None,
    ):
        self._element = element
        self._incoming_edges = incoming_edges or EdgeStackService()
        self._outgoing_edges = outgoing_edges or EdgeStackService()
        
        self._priority = None
        self._predecessor = None
        self._discovery_status = DiscoveryStatus.UNKNOWN
        
    @property
    def element(self) -> Element:
        return self._element
    
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
    def predecessor(self) -> Optional[Node[T]]:
        return self._predecessor
    
    @predecessor.setter
    def predecessor(self, predecessor: Node[T]):
        self._predecessor = predecessor
        
    