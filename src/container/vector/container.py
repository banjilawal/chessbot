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
        -   Data protection

    Responsibilities:
        1.  Immutable unordered set of vectors.

    Attributes:
        items: Tuple[Vector, ...]

    Provides:

    Super Class:
        Container
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
        