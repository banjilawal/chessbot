# src/chess/node/node.py

"""
Module: chess.edge.edge
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from __future__ import annotations

from chess.node import Node


class Edge:
    _label: int
    _head: Node
    _tail: Node
    _weight: int
    _distance: int
    _heuristic: int
    
    def __init__(
            self,
            label: int, 
            head: Node,
            tail: Node,
            distance: int,
            heuristic: int
    ):
        self._label = label
        self._head = head
        self._tail = tail
        self._distance = distance
        self._heuristic = heuristic
        self._weight = distance + heuristic
        
    @property
    def label(self) -> int:
        return self._label
    
    @property
    def head(self) -> Node:
        return self._head
    
    @property
    def tail(self) -> Node:
        return self._tail
    
    @property
    def distance(self) -> int:
        return self._distance
    
    @property
    def heuristic(self) -> int:
        return self._heuristic
    
    @heuristic.setter
    def heuristic(self, value: int):
        self._heuristic = value
    
    @property
    def weight(self) -> int:
        return self._weight
    
    @weight.setter
    def weight(self, value: int):
        self._weight = value
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Edge):
            return other.head == self._head and other.tail == self._tail
        return False
    
    def __hash__(self):
        return hash(self._label)
    
    
    