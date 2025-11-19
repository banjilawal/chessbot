# src/chess/piece/stack/stack.py

"""
Module: chess.piece.stack.stack
Author: Banji Lawal
Created: 2025-09-03
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord


class CoordStack:
    """
    # ROLE: Data Holding

    # RESPONSIBILITIES:
    Stores the Coords a Piece has visited.

    # PROVIDES:
    CoordStack

    # ATTRIBUTES:
        *   size (int)
        *   items (list[Coord])
        *   current_coord (Optional[Coord]):
    """
    _size: int
    _items: list[Coord]
    _current_coord: Optional[Coord]
    
    def __init__(self):
        self._items = list[Coord]
        self._size = len(self._items)
        self._current_coord = self._items[-1] if self._items else None
    
    @property
    def size(self) -> int:
        return len(self._items)
    
    @property
    def items(self) -> list[Coord]:
        return self._items
    
    @property
    def current_coord(self) -> Optional[Coord]:
        return self._items[-1] if self._items else None
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
