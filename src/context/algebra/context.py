from __future__ import annotations

from typing import Any, Dict, Optional

from geometry import Coord, Vector


class AlgebraAcontext:
    _vector: Optional[Vector]
    _coord: Optional[Coord]
    
    def __init__(
            self,
            vector: Optional[Vector] = None,
            coord: Optional[Coord] = None,
    ):
        """
        Args:
            vector: Optional[Vector]
            coord: Optional[Coord]
        """
        self._vector = vector
        self._coord = coord
        
    @property
    def vector(self) -> Optional[Vector]:
        return self._vector
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "vector": self._vector,
            "coord": self._coord,
        }