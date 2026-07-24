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
from space import QuadrantSpace


class QuadrantSet(Container[QuadrantSpace]):
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
    
    def __init__(self, items: Optional[Tuple[QuadrantSpace, ...]] | None = None):
        """
        Args:
            items: Optional[Tuple[Quadrant, ...]]
        """
        super().__init__(items=items)
        
    @property
    def items(self) -> Tuple[QuadrantSpace, ...]:
        return cast(Tuple[QuadrantSpace, ...], super().items)
    
    @property
    def iterator(self) -> Iterator[QuadrantSpace]:
        return iter(self.items)
    
    @property
    def to_list(self) -> List[QuadrantSpace]:
        return [item for item in self._items]

        