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
        
    Responsibilities:
        1.  Lists a Knight's possible destinations from its current postion.

    Attributes:
        termini: Tuple[T, ...]

    Provides:

    Super Class:
    """
    _entries: Tuple[T, ...]
    
    def __init__(self, entries: Optional[Tuple[T, ...]] | None = None):
        self._entries = entries or ()
        
    @property
    def entries(self) -> Tuple[T, ...]:
        return self._entries
    
    @property
    def size(self) -> int:
        return len(self._entries)
    
    @property
    def iterator(self) -> Iterator[T]:
        return iter(self._entries)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
        