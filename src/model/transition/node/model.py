# src/model/event/node/model.py

"""
Module: model.event.node.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional

from model import EventTransition, DiscoveryStatus, Node, Square


class NodeEventTransition(EventTransition[Node]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Node attribute-value tuple which selects an execution path.

    Attributes:
        priority: Optional[int]
        square: Optional[Square]
        predecessor: Optional[Node]
        discovery_status: Optional[DiscoveryStatus]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        EventTransition
    """
    priority: Optional[int] = None
    square: Optional[Square] = None
    predecessor: Optional[Node] = None
    discovery_status: Optional[DiscoveryStatus] = None
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "priority": self.priority,
            "square": self.square,
            "predecessor": self.predecessor,
            "discovery_status": self.discovery_status,
        }