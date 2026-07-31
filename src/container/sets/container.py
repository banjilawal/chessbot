# src/container/container.py

"""
Module: container.container
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Iterator, Optional, Tuple, TypeVar


T = TypeVar("T")

class Container(ABC, Generic[T]):
    """
    Role:
        -   Data Holder
        -   Data protection
        
    Responsibilities:
        1.  Immutable unordered set of items.

    Attributes:
        items: Tuple[T, ...]

    Provides:

    Super Class:
    """
    _items: Tuple[T, ...]
    
    def __init__(self, items: Optional[Tuple[T, ...]] | None = None):
        self._items = items or ()
        
    @property
    def items(self) -> Tuple[T, ...]:
        return self._items
    
    @property
    def size(self) -> int:
        return len(self._items)
    
    @property
    def iterator(self) -> Iterator[T]:
        return iter(self._items)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
        