# src/model/ray/vector/model.py

"""
Module: model.ray.vector.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Iterator, Optional, cast

from model import Coord, CoordRay, Ray, Vector
from model.ray.model import T


class VectorRay(Ray[Vector]):
    
    def __init__(self, origin: Optional[Vector] | None = None,):
        """
        Args:
            origin: Vector
        """
        super().__init__(origin=origin)
    
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
        return super().is_cycle and self.origin == self.terminus
    
    def have_same_origin(self, other: Ray[Vector]) -> bool:
        if not super().have_same_origin(other):
            return False
        if not isinstance(other, VectorRay):
            return False
        ray = cast(VectorRay, other)
        return self.origin == ray.origin
    
    def origins_are_different(self, other) -> bool:
        return not self.have_same_origin()
    
    def have_same_terminus(self, other) -> bool:
        if not super().have_same_origin(other):
            return False
        if not isinstance(other, VectorRay):
            return False
        ray = cast(VectorRay, other)
        return self.terminus == ray.terminus_is_different()
    
    def terminus_is_different(self, ray: Ray[T]) -> bool:
        return not self.have_same_terminus()
    
    def add_point(self, point: Vector):
        self._points.append(point)
        
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
    
        
    
        