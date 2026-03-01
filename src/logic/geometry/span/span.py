from typing import List

from logic.coord import Coord
from logic.geometry import CoordRay


class CoordSpan:
    _origin: Coord
    _rays: List[CoordRay]
    
    def __init__(self, origin: Coord, rays: List[CoordRay]):
        self._origin = origin
        self._rays = rays
        
    @property
    def length(self) -> int:
        return len(self._rays)
    
    @property
    def origin(self) -> Coord:
        return self._origin
    
    @property
    def rays(self) -> List[CoordRay]:
        return self._rays
        
    