#  src/domain/metadata/blueprint/context/graph/station/context.py

"""
Module: domain.metadata.blueprint.context.graph.station
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import GraphContext, Node, Station


class StationNodeContext(GraphContext[Station]):
        """
    Role:
        - Option Selector
    
        Responsibilities:
            1.  Supply a Station attribute-value search filter.
    
        Attributes:
            payload: Optional[Node]
            priority: Optional[int]
    
        Provides:
            -  to_dict() -> Dict[str, Any]
    
        Super Class:
            Context
        """
        _payload: Optional[Node]
        _priority: Optional[int]
        
        def __init__(
            self,
            payload: Optional[Node] | None = None,
            priority: Optional[int] | None = None,
        ):
            """
            Args:
                payload: Optional[Node]
                priority: Optional[int]
            """
            super().__init__()
            self._payload = payload
            self._priority = priority
        
        @property
        def priority(self) -> Optional[int]:
            return self._priority
        
        @property
        def payload(self) -> Optional[Node]:
            return self._payload
    
        @property
        def to_dict(self) -> Dict[str, Any]:
            return {
                "priorityy:": self._priority,
                "node": self._payload,
            }