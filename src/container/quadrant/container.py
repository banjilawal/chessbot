# src/container/quadrant/container.py

"""
Module: container.quadrant.container
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Iterator, List, Optional, Tuple, cast

from container import Container
from geometry.space import Quadrant


class QuadrantSet(Container[Quadrant]):
    """
    Role:
        -   Data Holder
        -   Data protection

    Responsibilities:
        1.  Immutable unordered set of quadrants.

    Attributes:
        items: Tuple[Quadrant, ...]

    Provides:

    Super Class:
        Container
    """
    
    def __init__(self, items: Optional[Tuple[Quadrant, ...]] | None = None):
        """
        Args:
            items: Optional[Tuple[Quadrant, ...]]
        """
        super().__init__(items=items)
        
    @property
    def items(self) -> Tuple[Quadrant, ...]:
        return cast(Tuple[Quadrant, ...], super().items)
    
    @property
    def iterator(self) -> Iterator[Quadrant]:
        return iter(self.items)
    
    @property
    def to_list(self) -> List[Quadrant]:
        return [item for item in self._items]

        