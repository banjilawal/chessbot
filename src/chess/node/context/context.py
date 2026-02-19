# src/chess/node/context/context.py

"""
Module: chess.node.context.context
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from chess.square import Square
from chess.system import Context
from chess.node import DiscoveryStatus, Node


class NodeContext(Context[Node]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    Provide an NodeFinder with an attribute value to find Nodes with a matching value in teir version of
    the attribute.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   priority (Optional[Priority])
        *   square (Optional[Square])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
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
        # RAISES:
        None
        """
        return {
            "priority": self._priority,
            "square": self._square,
            "predecessor": self._predecessor,
            "discovery_status": self._discovery_status,
        }