# src/node/vector/node.py

"""
Module: node.vector.node
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.model import Vector
from domain.structure.node import Node


class VectorNode(Node[Vector]):
    
    def __init__(self, payload: Optional[Vector] | None = None):
        super().__init__(payload=payload)
        
    @property
    def payload(self) -> Vector:
        return cast(Vector, super().payload)
    
    @property
    def next(self) -> Optional[VectorNode]:
        return cast(VectorNode, super().next)
    
    @next.setter
    def next(self, other: VectorNode):
        super().next = other
    
    @property
    def previous(self) -> Optional[VectorNode]:
        return cast(VectorNode, super().previous)
    
    @previous.setter
    def previous(self, other: VectorNode):
        super().previous = other
        
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, VectorNode):
            node = cast(VectorNode, other)
            return self.payload == node.payload
        return False
    
    