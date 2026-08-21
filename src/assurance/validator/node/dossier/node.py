# src/node/dossier/node.py

"""
Module: node.dossier.node
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.model import Dossier
from domain.node import Node


class DossierNode(Node[Dossier]):
    
    def __init__(self, payload: Optional[Dossier] | None = None):
        super().__init__(payload=payload)
        
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
    
    