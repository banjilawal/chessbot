# src/domain/graph/edge/component.py

"""
Module: domain.graph.edge.component
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import GraphComponent, Station


class Edge(GraphComponent):
    _label: int
    _head: Station
    _tail: Station
    _distance: int
    _weight: Optional[int]
    _heuristic: Optional[int]
    
    def __init__(
            self,
            label: int, 
            head: Station,
            tail: Station,
            distance: int,
            weight: Optional[int] | None = None,
            heuristic: Optional[int] | None = None,
    ):
        """
        Args:
            label: int
            head: Station
            tail: Station
            distance: int
            weight: Optional[int]
            heuristic: Optional[int]
        """
        self._label = label
        self._head = head
        self._tail = tail
        self._distance = distance
        self._weight = weight
        self._heuristic = heuristic
        
    @property
    def label(self) -> int:
        return self._label
    
    @property
    def head(self) -> Station:
        return self._head
    
    @property
    def tail(self) -> Station:
        return self._tail
    
    @property
    def distance(self) -> int:
        return self._distance
    
    @property
    def heuristic(self) -> Optional[int]:
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
    
    
    