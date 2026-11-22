# src/domain/struct/node/vector/struct.py

"""
Module: domain.struct.node.vector.struct
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, cast

from domain import Node, Vector


class VectorNode(Node[Vector]):
    """
    Role:
        - Structural Wrapper

    Responsibilities:
        1.  Encapsulate a Vector payload with pointer references (next/previous) to
            enable doubly-linked traversal.
        2.  Provide type-safe accessors for payload inspection and node chaining.

    Attributes:
        content: Optional[Vector]
        next: Optional[VectorNode]
        previous: Optional[VectorNode]
        
    Provides:

    Super Class:
        Node
    """
    
    def __init__(
            self,
            content: Optional[Vector] | None = None,
            next: Optional[VectorNode] | None = None,
            previous: Optional[VectorNode] | None = None,
    ):
        """
        Args:
            content: Optional[Vector]
            next: Optional[VectorNode]
            previous: Optional[VectorNode]
        """
        super().__init__(content=content, next=next, previous=previous)

        
    @property
    def content(self) -> Optional[Vector]:
        return cast(Vector, super().content)
    
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
    
    @property
    def to_dict(self) -> Dict[str, Vector]:
        table = {}
        
        content = self.content
        if content is not None:
            table["content"] = content
        next = self.next
        previous = self.previous
        if next is not None and next.content is not None:
            table["next_vector"] = next.content
        if previous is not None and previous.content is not None:
            table["previous_vector"] = previous.content
        return table
        
        
        
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, VectorNode):
            return self.content == other.content
        return False
    
    