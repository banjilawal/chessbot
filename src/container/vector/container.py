# src/container/vector/container.py

"""
Module: container.vector.container
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Iterator, List, Optional, Tuple, cast

from container import Container
from model import Coord, Vector


class VectorSet(Container[Vector]):
    """
    Role:
        -   Data Holder
        
    Responsibilities:
        1.  A bag of vectors whose order is not guaranteed.

    Attributes:
        entries: Tuple[Vector, ...]

    Provides:

    Super Class:
        Container
    """
    
    def __init__(self, entries: Optional[Tuple[Vector, ...]] | None = None):
        """
        Args:
            entries: Optional[Tuple[Vector, ...]]
        """
        super().__init__(entries=entries)
        
    @property
    def entries(self) -> Tuple[Vector, ...]:
        return cast(Tuple[Vector, ...], self.entries)
    
    @property
    def iterator(self) -> Iterator[Vector]:
        return iter(self.entries)
    
    @property
    def to_list(self) -> List[Vector]:
        return [entry for entry in self._entries]
    
    def to_coord_tuple(self) -> Tuple[Coord, ...]:
        return tuple(Coord(column=entry.x, row=entry.y) for entry in self._entries)
        