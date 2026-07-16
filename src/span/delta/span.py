# src/span/delta/knight/span.py

"""
Module: span.delta.knight.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Iterator, List, Optional, Tuple, TypeVar

from model import Coord, Vector

T = TypeVar("T", bounds="Rank")

class VectorSet(ABC, Generic[T]):
    """
    Role:
        -   Data Holder
        
    Responsibilities:
        1.  Lists a Knight's possible destinations from its current postion.

    Attributes:
        termini: Tuple[Vector, ...]

    Provides:

    Super Class:
    """
    _entries: Tuple[Vector, ...]
    
    def __init__(self, entries: Optional[Tuple[Vector, ...]] | None = None):
        self._entries = entries or ()
        
    @property
    def entries(self) -> Tuple[Vector, ...]:
        return self._entries
    
    @property
    def size(self) -> int:
        return len(self._entries)
    
    @property
    def iterator(self) -> Iterator[Vector]:
        return iter(self._entries)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def is_a_point(self) -> bool:
        return self.size == 1
    
    @property
    def is_linear(self) -> bool:
        return self.size >= 2
    
    def to_coords(self) -> Tuple[Coord, ...]:
        return tuple(Coord(column=entry.x, row=entry.y) for entry in self._entries)
        