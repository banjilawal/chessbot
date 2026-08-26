# src/domain/structure/node/structure.py

"""
Module: domain.structure.node.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from domain import DataModel, Structure

T = TypeVar("T", bound="DataModel")


class Node(Structure, ABC, Generic[T]):
    """
    Role:
        - Structural Wrapper

    Responsibilities:
        1.  Encapsulate a domain Model payload with pointer references (next/previous) to
            enable doubly-linked traversal.
        2.  Provide type-safe accessors for payload inspection and node chaining.

    Attributes:
        payload: T
        next: Optional[Node[T]]
        previous: Optional[Node[T]]
        
    Provides:

    Super Class:
    """
    _payload: Optional[T]
    _next: Optional[Node[T]]
    _previous: Optional[Node[T]]
    
    def __init__(
            self,
            payload: T,
            next: Optional[Node[T]] | None = None,
            previous: Optional[Node[T]] | None = None,
    ):
        """
        Args:
            payload: T
            next: Optional[Node[T]]
            previous: Optional[Node[T]]
        """
        self._payload = payload
        self._next = next
        self._previous = previous
    
    @property
    def payload(self) -> Optional[T]:
        return self._payload
    
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
    def is_blank(self) -> bool:
        return (
                self._payload is None and
                self.does_not_have_orphan_pointers
        )
    
    @property
    def is_not_blank(self):
        return not self.is_blank
    
    @property
    def is_consistent(self) -> bool:
        return self.does_not_have_orphan_pointers
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.is_consistent
    
    @property
    def has_orphan_pointers(self) -> bool:
        return self._payload is None and self.has_neighbors 
    
    @property
    def does_not_have_orphan_pointers(self) -> bool:
        return self._payload is not None and self.has_orphan_pointers 
    
    @property
    def has_neighbors(self) -> bool:
        return self.number_of_pointers > 0
    
    @property
    def does_not_have_neighbors(self) -> bool:
        return not self.has_neighbors
    
    @property
    def number_of_pointers(self) -> int:
        return len([self._next, self._previous])
    
    
        
