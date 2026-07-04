# src/model/state/node/model/state.py

"""
Module: model.state.node.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from stack import EdgeStackService
from model import DiscoveryStatus, Square


class Node:
    _priority: int
    _square: Square
    _predecessor:Optional[Node]
    _incoming_edges: EdgeStackService
    _outgoing_edges: EdgeStackService
    _discovery_status: DiscoveryStatus    
    def __init__(self, square: Square):
        self._square = square
        
        self._priority = 0
        self._predecessor = None
        self._incoming_edges = EdgeStackService()
        self._outgoing_edges = EdgeStackService()
        self._discovery_status = DiscoveryStatus.UNKNOWN
        
    @property
    def square(self) -> Square:
        return self._square
    
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
    def priority(self) -> int:
        return self._priority
    
    @priority.setter
    def priority(self, priority: int):
        self._priority = priority
        
    @property
    def predecessor(self) -> Node:
        return self._predecessor
    
    @predecessor.setter
    def predecessor(self, predecessor: Node):
        self._predecessor = predecessor
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Node): return self.square == other.square
        return False
    
    def __hash__(self):
        return hash(self.square)
        
    