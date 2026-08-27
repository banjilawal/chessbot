# src/operation/toolkit/collection/sets/coord/set.py

"""
Module: operation.toolkit.collection.sets.coord.set
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Iterator, List, Optional, Tuple, cast

from collection import SetCollection
from domain.model import Coord, Vector


class CoordSet(SetCollection[Coord]):
    """
    Role:
        - Data Holder
        -  Data protection

    Responsibilities:
        1.  Immutable unordered set of coords.

    Attributes:
        items: Tuple[Coord, ...]

    Provides:

    Super Class:
        Collection
    """
    
    def __init__(self, items: Optional[Tuple[Coord, ...]] | None = None):
        """
        Args:
            items: Optional[Tuple[Coord, ...]]
        """
        super().__init__(items=items)
        
    @property
    def items(self) -> Tuple[Coord, ...]:
        return cast(Tuple[Coord, ...], super().items)
    
    @property
    def iterator(self) -> Iterator[Coord]:
        return iter(self.items)
    
    @property
    def to_list(self) -> List[Coord]:
        return [item for item in self._items]
    
    def to_vector_tuple(self) -> Tuple[Vector, ...]:
        return tuple(Vector(x=item.column, y=item.row) for item in self._items)
        