# src/chess/square_name/map.py

"""
Module: chess.square_name.map
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.square import Square
from chess.system import Context


class SquareContext(Context[Square]):
    _coord: Optional[Coord] = None
    
    def __init__(
            self,
            id: Optional[int],
            name: Optional[str],
            coord: Optional[Coord] = None
    ):
        super().__init__(id=id, name=name)
        self._coord = coord
        
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "designation": self.name,
            "coord": self._coord
        }