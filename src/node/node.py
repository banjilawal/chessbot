# src/node/node.py

"""
Module: node.node
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from model import Model

T = TypeVar("T", bound="Model")


class Node(ABC, Generic[T]):
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
    _payload: T
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
    def payload(self) -> T:
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
