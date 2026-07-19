# src/container/register/container.py

"""
Module: container.register.container
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Iterator, Optional, Tuple, cast

from container import Container
from register import Register


class RegisterSet(Container[Register]):
    """
    Role:
        -   Data Holder
        
    Responsibilities:
        1.  A bag of registers whose order is not guaranteed.

    Attributes:
        entries: Tuple[Register, ...]

    Provides:

    Super Class:
        Container
    """
    
    def __init__(self, entries: Optional[Tuple[Register, ...]] | None = None):
        """
        Args:
            entries: Optional[Tuple[Register, ...]]
        """
        super().__init__(entries=entries)
        
    @property
    def entries(self) -> Tuple[Register, ...]:
        return cast(Tuple[Register, ...], self.entries)
    
    @property
    def iterator(self) -> Iterator[Register]:
        return iter(self.entries)
    
    def to_coord_tuple(self) -> Tuple[Coord, ...]:
        return tuple(Coord(column=entry.x, row=entry.y) for entry in self._entries)
        