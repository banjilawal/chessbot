# src/domain/struct/node/struct.py

"""
Module: domain.struct.node.struct
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, TypeVar

from domain import Struct
from domain import SearchableModel

T = TypeVar("T", bound="SearchableModel")


class Node(Struct[T], Generic[T]):
    """
    Role:
        - Structural Wrapper

    Responsibilities:
        1.  Encapsulate a domain Model payload with pointer references (next/previous) to
            enable doubly-linked traversal.
        2.  Provide type-safe accessors for payload inspection and node chaining.

    Attributes:
        content: Optional[T]
        next: Optional[Node[T]]
        previous: Optional[Node[T]]
        
    Provides:

    Super Class:
    """
    
    _content: Optional[T]
    _next: Optional[Node[T]]
    _previous: Optional[Node[T]]
    
    def __init__(
            self,
            content: Optional[T] | None = None,
            next: Optional[Node[T]] | None = None,
            previous: Optional[Node[T]] | None = None,
    ):
        """
        Args:
            content: Optional[T],
            next: Optional[Node[T]]
            previous: Optional[Node[T]]
        """
        self._content = content
        self._next = next
        self._previous = previous
    
    @property
    def content(self) -> Optional[T]:
        return self._content
    
    @property
    def next(self) -> Optional[Node[T]]:
        return self._next
    
    @next.setter
    def next(self, other: Node[T]):
        self._next = other
    
    @property
    def previous(self) -> Optional[Node[T]]:
        return self._previous
    
    @previous.setter
    def previous(self, other: Node[T]):
        self._previous = other
        
    @property
    def is_empty(self) -> bool:
        return (
                self._content is None and
                self.does_not_have_orphan_pointers
        )
    
    @property
    def is_not_empty(self):
        return not self.is_empty
    
    @property
    def is_consistent(self) -> bool:
        return self.does_not_have_orphan_pointers
    
    @property
    def size(self) -> int:
        return len([self._content]) + self.length
    
    @property
    def number_of_pointers(self) -> int:
        return len([self._next, self._previous])

    @property
    def has_orphan_pointers(self) -> bool:
        return self._content is None and self.has_neighbors
    
    @property
    def does_not_have_orphan_pointers(self) -> bool:
        return not self.has_orphan_pointers
    
    @property
    def has_neighbors(self) -> bool:
        return self.number_of_pointers > 0
    
    @property
    def does_not_have_neighbors(self) -> bool:
        return not self.has_neighbors
    
    @property
    def to_dict(self) -> Dict[str, T]:
        return {}
    
    @property
    def length(self) -> int:
        rear_nodes = 0
        vanguard_nodes = 0
        
        head_cursor = self.next
        while head_cursor is not None:
            vanguard_nodes = vanguard_nodes + 1
            head_cursor = head_cursor.next
            
        tail_cursor = self.previous
        while tail_cursor is not None:
            rear_nodes = rear_nodes + 1
            tail_cursor = tail_cursor.previous
        total_nodes = rear_nodes + vanguard_nodes
        
        