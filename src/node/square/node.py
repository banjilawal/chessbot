# src/node/square/node.py

"""
Module: node.square.node
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from model import Square
from node import DiscoveryStatus, Node
from stack import EdgeStackService


class SquareNode(Node[Square]):
    _priority: int
    _square: Square
    _predecessor:Optional[SquareNode]
    _incoming_edges: EdgeStackService
    _outgoing_edges: EdgeStackService
    _discovery_status: DiscoveryStatus
    
    def __init__(
            self,
            element: Square,
            incoming_edges: EdgeStackService | None = EdgeStackService(),
            outgoing_edges: EdgeStackService | None = EdgeStackService(),
    ):
        super().__init__(
            element=element,
            incoming_edges=incoming_edges,
            outgoing_edges=outgoing_edges,
        )
        
    @property
    def element(self) -> Square:
        return cast(Square, self._element)
    
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
    def predecessor(self) -> SquareNode:
        return self._predecessor
    
    @predecessor.setter
    def predecessor(self, predecessor: SquareNode):
        self._predecessor = predecessor
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SquareNode):
            node = cast(SquareNode)
            return self.element == node.element
        return False
    
    def __hash__(self):
        return hash(self.element.__hash__())
        
    