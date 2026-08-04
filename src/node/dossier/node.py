# src/node/node.py

"""
Module: node.node
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from model import SquareDossier
from node import Node


class SquareDossierNode(Node[SquareDossier]):
    
    def __init__(self, payload: SquareDossier):
        super().__init__(payload=payload)
        
    @property
    def payload(self) -> SquareDossier:
        return cast(SquareDossier, super().payload)
    
    @property
    def next(self) -> Optional[SquareDossierNode]:
        return cast(SquareDossierNode, super().next)
    
    @next.setter
    def next(self, other: SquareDossierNode):
        super().next = other
    
    @property
    def previous(self) -> Optional[SquareDossierNode]:
        return cast(SquareDossierNode, super().previous)
    
    @previous.setter
    def previous(self, other: SquareDossierNode):
        super().previous = other
    
    