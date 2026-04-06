# src/model/context/node/model.py

"""
Module: model.context.node.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class NodeContext(Context[Node]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Node attribute-value tuple which selects an execution path.

    Attributes:
        id: Optional[int]
        team: Optional[Team]
        rank: Optional[Rank]
        ransom: Optional[int]
        current_position:Optional[Coord]
        designation: Optional[str]
        color: Optional[GameColor]
        opening_square_name: Optional[str]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    _priority: Optional[int]
    _square: Optional[Square]
    _predecessor: Optional[Node]
    _discovery_status: Optional[DiscoveryStatus]
    
    def __init__(
            self,
            priority: Optional[int] = None,
            square: Optional[Square] = None,
            predecessor: Optional[Node] = None,
            discovery_status: Optional[DiscoveryStatus] = None,
    ):
        super().__init__(id=None, name=None)
        self._priority = priority
        self._square = square
        self._predecessor = predecessor
        self._discovery_status = discovery_status
        
    @property
    def priority(self) -> Optional[int]:
        return self._priority
        
    @property
    def square(self) -> Optional[Square]:
        return self._square
    
    @property
    def predecessor(self) -> Optional[Node]:
        return self._predecessor
    
    @property
    def discovery_status(self) -> Optional[DiscoveryStatus]:
        return self._discovery_status
    
    def to_dict(self) -> dict:
        """
        # ACTION:
        Convert a NodeContext attributes into a dictionary.
        # PARAMETERS:
        None
        # RETURNS:
            dict
        Raises:
        """
        return {
            "priority": self._priority,
            "square": self._square,
            "predecessor": self._predecessor,
            "discovery_status": self._discovery_status,
        }