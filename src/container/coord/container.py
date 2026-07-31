# src/container/coord/container.py

"""
Module: container.coord.container
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Iterator, List, Optional, Tuple, cast

from container import Container
from model import Coord, Coord, Vector


class CoordSet(Container[Coord]):
    """
    Role:
        -   Data Holder
        -   Data protection

    Responsibilities:
        1.  Immutable unordered set of coords.

    Attributes:
        items: Tuple[Coord, ...]

    Provides:

    Super Class:
        Container
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
        