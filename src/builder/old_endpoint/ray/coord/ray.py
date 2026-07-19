# src/space/ray/coord/space/ray.py

"""
Module: space.ray.coord.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Iterator, List, Optional, cast

from model import Coord
from space import Ray


class CoordRay(Ray[Coord]):
    """
    Role:
        -   DTO, Data Holder
        -   Transform

    Responsibilities:
        1.  List of Coords in order of discovery on a line.
        2.  Resource for a GraphFactory needs for creating Edge and Node products.
        3.  No direct access to the list.

    Attributes:
        origin: Optional[Coord]
        terminus: Optional[Coord]
        iterator: Iterator[Coord]:
        is_empty: bool
        is_cycle: bool
        size: int

    Provides:
        -   def add_point(point: Coord)
        -   def to_coord_ray() -> CoordRay
        
        -   def have_same_origin(other) -> bool
        -   def origins_are_different(other) -> bool
        
        -   def have_same_terminus(other) -> bool
        -   def terminus_is_different(other) -> bool

    Super Class:
        Ray
        
    WARNING:
        *****===DOES NOT GUARANTEE UNIQUENESS, INTEGRITY OR CONSISTENCY===*****
    """
    
    def __init__(self, points: Optional[List[Coord]]):
        """
        Args:
            points: List[Coord]
        """
        super().__init__(points=points)
        if points is None:
            points = []
    
    @property
    def origin(self) -> Optional[Coord]:
        return cast(Coord, self.origin)
    
    @property
    def terminus(self) -> Optional[Coord]:
        return cast(Coord, self.terminus)
    
    @property
    def iterator(self) -> Iterator[Coord]:
        return iter(self._points)
    
    @property
    def is_cycle(self) -> bool:
        if not super().is_cycle:
            return False
        return self.origin == self.terminus
    
    @property
    def is_not_cycle(self) -> bool:
        return not self.is_cycle
    
    def add_point(self, point: Coord):
        self._points.append(point)
    
    def have_same_origin(self, other: Ray[Coord]) -> bool:
        if not super().have_same_origin(other):
            return False
        if not isinstance(other, CoordRay):
            return False
        ray = cast(CoordRay, other)
        return self.origin == space.ray.origin
    
    def have_same_terminus(self, other) -> bool:
        if not super().have_same_origin(other):
            return False
        if not isinstance(other, CoordRay):
            return False
        ray = cast(CoordRay, other)
        return self.terminus == space.ray.terminus
    
    def origins_are_different(self, other) -> bool:
        return not self.have_same_origin(other)
    
    def termini_are_different(self, other) -> bool:
        return not self.have_same_terminus(other)

        
    def to_coord_ray(self) -> CoordRay:
        
        ray = CoordRay(
            origin=Coord(
                column=self.origin.x,
                row=self.origin.y,
            )
        )
        for point in self._points:
            ray.add_point(Coord(column=point.x, row=point.y))
        return ray
    
        
    
        