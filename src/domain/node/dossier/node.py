# src/domain/node/dossier/domain/node.py

"""
Module: domain.node.dossier.node
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.model import Dossier
from domain.node import Node


class DossierNode(Node[Dossier]):
    """
    Role:
        - Structural Wrapper

    Responsibilities:
        1.  Encapsulate a Dossier  payload with pointer references (next/previous) to
            enable doubly-linked traversal.
        2.  Provide type-safe accessors for payload inspection and node chaining.

    Attributes:
        payload: Dossier
        next: Optional[DossierNode]
        previous: Optional[DossierNode]
        
    Provides:

    Super Class:
        Node
    """
    
    def __init__(self, payload: Dossier):
        super().__init__(payload=payload)
        super().next = None
        super.previous = None
        
    @property
    def payload(self) -> Dossier:
        return cast(Dossier, super().payload)
    
    @property
    def next(self) -> Optional[DossierNode]:
        return cast(DossierNode, super().next)
    
    @next.setter
    def next(self, other: DossierNode):
        super().next = other
    
    @property
    def previous(self) -> Optional[DossierNode]:
        return cast(DossierNode, super().previous)
    
    @previous.setter
    def previous(self, other: DossierNode):
        super().previous = other
        
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, DossierNode):
            node = cast(DossierNode, other)
            return self.payload == domain.node.payload
        return False
    
    