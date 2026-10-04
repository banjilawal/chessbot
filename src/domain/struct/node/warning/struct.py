# src/domain/struct/node/warning/struct.py

"""
Module: domain.struct.node.warning.struct
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterWarning, Node


class WarningNode(Node[EncounterWarning]):
    """
    Role:
        - Structural

    Responsibilities:
        1.  Encapsulate a Warning  payload with pointer references (next/previous) to
            enable doubly-linked traversal.
        2.  Provide type-safe accessors for payload inspection and node chaining.

    Attributes:
        payload: Warning
        next: Optional[WarningNode]
        previous: Optional[WarningNode]
        
    Provides:

    Super Class:
        Node
    """
    
    def __init__(self, payload: EncounterWarning):
        super().__init__(payload=payload)
        super().next = None
        super.previous = None
        
    @property
    def payload(self) -> EncounterWarning:
        return cast(EncounterWarning, super().payload)
    
    @property
    def next(self) -> Optional[WarningNode]:
        return cast(WarningNode, super().next)
    
    @next.setter
    def next(self, other: WarningNode):
        super().next = other
    
    @property
    def previous(self) -> Optional[WarningNode]:
        return cast(WarningNode, super().previous)
    
    @previous.setter
    def previous(self, other: WarningNode):
        super().previous = other
        
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, WarningNode):
            return self.payload == other.payload
        return False
    
    