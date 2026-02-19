# src/chess/node/node.py

"""
Module: chess.node.node
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from __future__ import annotations

from chess.square import Square
from chess.edge import EdgeStack
from chess.node import DiscoveryStatus

class Node:
    _priority: int
    _square: Square
    _predecessor: Node
    _incoming_edges: EdgeStack
    _outgoing_edges: EdgeStack
    _discovery_status: DiscoveryStatus

    
    def __init__(self, square: Square):
        self._square = square
        
        self._priority = 0
        self._predecessor = None
        self._incoming_edges = EdgeStack()
        self._outgoing_edges = EdgeStack()
        self._discovery_status = DiscoveryStatus.UNKNOWN
        
    @property
    def square(self) -> Square:
        return self._square
    
    @property
    def incoming_edges(self) -> EdgeStack:
        return self._incoming_edges
    
    @property
    def outgoing_edges(self) -> EdgeStack:
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
        
    