# src/space/ray/vector/space/ray.py

"""
Module: space.ray.vector.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Iterator, List, Optional, cast

from model import Coord, Vector
from space.ray import CoordRay, Ray


class VectorRay(Ray[Vector]):
    """
    Role:
        -   DTO, Data Holder
        -   Transform

    Responsibilities:
        1.  List of Vectors in order of discovery on a line.
        2.  Resource for a GraphFactory needs for creating Edge and Node products.
        3.  No direct access to the list.

    Attributes:
        origin: Optional[Vector]
        terminus: Optional[Vector]
        iterator: Iterator[Vector]:
        is_empty: bool
        is_cycle: bool
        size: int

    Provides:
        -   def add_point(point: Vector)
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
    
    def __init__(
            self,
            points: Optional[List[Vector]] | None = None
    ):
        """
        Args:
            points: List[Vector]
        """
        super().__init__(points=points)
    
    @property
    def origin(self) -> Optional[Vector]:
        return cast(Vector, self.origin)
    
    @property
    def terminus(self) -> Optional[Vector]:
        return cast(Vector, self.terminus)
    
    @property
    def iterator(self) -> Iterator[Vector]:
        return iter(self._points)
    
    @property
    def is_cycle(self) -> bool:
        if not super().is_cycle:
            return False
        return self.origin == self.terminus
    
    @property
    def is_not_cycle(self) -> bool:
        return not self.is_cycle
    
    def add_point(self, point: Vector):
        self._points.append(point)
    
    def have_same_origin(self, other: Ray[Vector]) -> bool:
        if not super().have_same_origin(other):
            return False
        if not isinstance(other, VectorRay):
            return False
        ray = cast(VectorRay, other)
        return self.origin == space.ray.origin
    
    def have_same_terminus(self, other) -> bool:
        if not super().have_same_origin(other):
            return False
        if not isinstance(other, VectorRay):
            return False
        ray = cast(VectorRay, other)
        return self.terminus == space.ray.terminus
    
    def origins_are_different(self, other) -> bool:
        return not self.have_same_origin(other)
    
    def termini_are_different(self, other) -> bool:
        return not self.have_same_terminus(other)

        
    def to_coord_ray(self) -> CoordRay:
        ray = CoordRay()
        for point in self._points:
            ray.add_point(Coord(column=point.x, row=point.y))
        return ray
    
        
    
        