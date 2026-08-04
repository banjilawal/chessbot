# src/node/vector/node.py

"""
Module: node.vector.node
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from model import Vector
from node import Node


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
    
    