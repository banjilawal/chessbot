# src/node/node.py

"""
Module: node.node
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(ABC, Generic[T]):
    _payload: T
    _next: Optional[Node[T]]
    _previous: Optional[T]
    
    
    def __init__(
            self,
            payload: T,
            next: Optional[Node[T] ]| None = None,
            previous: Optional[Node[T]] | None = None,
    ):
        self.payload = payload
        self._next = next
        self._previous = previous

    
    @property
    def payload(self) -> T:
        return self.payload
    
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
