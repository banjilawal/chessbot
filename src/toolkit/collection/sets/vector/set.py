# src/toolkit/collection/sets/vector/set.py

"""
Module: toolkit.collection.sets.vector.set
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Iterator, List, Optional, Tuple, cast

from collection import SetCollection
from model import Coord, Vector


class VectorSet(SetCollection[Vector]):
    """
    Role:
        -   Data Holder
        -   Data protection

    Responsibilities:
        1.  Immutable unordered set of vectors.

    Attributes:
        items: Tuple[Vector, ...]

    Provides:

    Super Class:
        Collection
    """
    
    def __init__(self, items: Optional[Tuple[Vector, ...]] | None = None):
        """
        Args:
            items: Optional[Tuple[Vector, ...]]
        """
        super().__init__(items=items)
        
    @property
    def items(self) -> Tuple[Vector, ...]:
        return cast(Tuple[Vector, ...], super().items)
    
    @property
    def iterator(self) -> Iterator[Vector]:
        return iter(self.items)
    
    @property
    def to_list(self) -> List[Vector]:
        return [item for item in self._items]
    
    def to_coord_tuple(self) -> Tuple[Coord, ...]:
        return tuple(Coord(column=item.x, row=item.y) for item in self._items)
    
    @property
    def to_coord_list(self) -> List[Coord]:
        return [Coord(column=item.x, row=item.y) for item in self.to_list]

        
        