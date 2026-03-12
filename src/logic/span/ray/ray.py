# src/logic/span/ray/ray.py

"""
Module: logic.span.ray.ray
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.coord import Coord

class CoordRay:
    """
    # ROLE: Data-Holder
    
    # RESPONSIBILITIES:
    1.  Stores points that define a ray from an origin to a terminus

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   origin: Coord
        *   points: List[Coord]

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:)
        *   origin: Coord
        *   points: List[Coord]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
    None
    """
    _origin: Coord
    _points: List[Coord]
    
    def __init__(self, origin: Coord, points: List[Coord]):
        """
        Args:
            origin: Coord
            points: List[Coord]
        """
        self._origin = origin
        self._points = points
        
    @property
    def origin(self) -> Coord:
        return self._origin
    
    @property
    def points(self) -> List[Coord]:
        return self._points
    
    @property
    def origin_inclusive_length(self) -> int:
        return len(self._points) + 1