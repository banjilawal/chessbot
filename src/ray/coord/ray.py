# src/ray/coord/ray.py

"""
Module: ray.coord.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Iterator, Optional, cast

from model import Coord, Ray, Vector, VectorRay
from ray.ray import T


class CoordRay(Ray[Coord]):
    
    def __init__(self, origin: Optional[Coord] | None = None):
        """
        Args:
            origin: Coord
        """
        super().__init__(origin=origin)
    
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
        return super().is_cycle and self.origin == self.terminus
    
    def have_same_origin(self, other) -> bool:
        if not super().have_same_origin(other):
            return False
        if not isinstance(other, CoordRay):
            return False
        ray = cast(CoordRay, other)
        return self.origin == ray.origin
    
    def origins_are_different(self, other) -> bool:
        return not self.have_same_origin(other)
    
    def have_same_terminus(self, other) -> bool:
        if not super().have_same_origin(other):
            return False
        if not isinstance(other, CoordRay):
            return False
        ray = cast(CoordRay, other)
        return self.terminus == ray.terminus
    
    def terminus_is_different(self, other) -> bool:
        return not self.have_same_terminus(other)
    
    def add_point(self, point: Coord):
        self._points.append(point)
        
    def to_vector_ray(self) -> VectorRay:
        ray = VectorRay(
            origin=Vector(
                x=self.origin.column,
                y=self.origin.row,
            )
        )
        for point in self._points:
            ray.add_point(Vector(x=point.column, y=point.row))
        return ray
    
        
    
        