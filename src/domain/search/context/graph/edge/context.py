# src/domain/search/context/graph/edge/context.py.py

"""
Module: domain.search.context.graph.edge.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import GraphSearchContext, Edge, Station


class EdgeSearchContext(GraphSearchContext[Edge]):
        """
        Role:
            -   Selection
            -   Routing mask
            -   Data-Holder
    
        Responsibilities:
            1.  Supply an Edge attribute-value search filter.
    
        Attributes:
            head: Optional[Station]
            tail: Optional[Station]
            label: Optional[int]
            weight: Optional[int]
            distance: Optional[int]
            heuristic: Optional[int]
    
        Provides:
            -   to_dict() -> Dict[str, Any]
    
        Super Class:
            Context
        """
        _head: Optional[Station]
        _tail: Optional[Station]
        _label: Optional[int]
        _weight: Optional[int]
        _distance: Optional[int]
        _heuristic: Optional[int]

        
        def __init__(
            self,
            head: Optional[Station] | None = None,
            tail: Optional[Station] | None = None,
            label: Optional[int] | None = None,
            weight: Optional[int] | None = None,
            distance: Optional[int] | None = None,
            heuristic: Optional[int] | None = None,
        ):
            """
            Args:
                head: Optional[Station]
                tail: Optional[Station]
                label: Optional[int]
                weight: Optional[int]
                distance: Optional[int]
                heuristic: Optional[int]
            """
            super().__init__()
            self._head = head
            self._tail = tail
            self._label = label
            self._weight = weight
            self._distance = distance
            self._heuristic = heuristic
        
        @property
        def head(self) -> Optional[Station]:
            return self._head
        
        @property
        def tail(self) -> Optional[Station]:
            return self._tail
        
        @property
        def label(self) -> Optional[int]:
            return self._label
        
        @property
        def weight(self) -> Optional[int]:
            return self._weight
        
        @property
        def distance(self) -> Optional[int]:
            return self._distance
        
        @property
        def heuristic(self) -> Optional[int]:
            return self._heuristic
    
        @property
        def to_dict(self) -> Dict[str, Any]:
            return {
                "head": self._head,
                "tail": self._tail,
                "label": self.label,
                "weight": self.weight,
                "distance": self.distance,
                "heuristic": self.heuristic,
            }