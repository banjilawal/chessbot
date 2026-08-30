# src/domain/structure/node/check/structure.py

"""
Module: domain.structure.node.check.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CheckEnemyKing, Node


class CheckNode(Node[CheckEnemyKing]):
    """
    Role:
        - Structural

    Responsibilities:
        1.  Encapsulate a Check  payload with pointer references (next/previous) to
            enable doubly-linked traversal.
        2.  Provide type-safe accessors for payload inspection and node chaining.

    Attributes:
        payload: Check
        next: Optional[CheckNode]
        previous: Optional[CheckNode]
        
    Provides:

    Super Class:
        Node
    """
    
    def __init__(self, payload: CheckEnemyKing):
        super().__init__(payload=payload)
        super().next = None
        super.previous = None
        
    @property
    def payload(self) -> CheckEnemyKing:
        return cast(CheckEnemyKing, super().payload)
    
    @property
    def next(self) -> Optional[CheckNode]:
        return cast(CheckNode, super().next)
    
    @next.setter
    def next(self, other: CheckNode):
        super().next = other
    
    @property
    def previous(self) -> Optional[CheckNode]:
        return cast(CheckNode, super().previous)
    
    @previous.setter
    def previous(self, other: CheckNode):
        super().previous = other
        
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, CheckNode):
            return self.payload == other.payload
        return False
    
    