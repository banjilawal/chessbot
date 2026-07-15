# src/ray/vector/ray.py

"""
Module: ray.vector.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Iterator, Optional, cast

from model import Coord, CoordRay, Ray, Vector
from ray.ray import T


class VectorRay(Ray[Vector]):
    """
    Role:
        -   DTO, Data Holder
        -   Transform

    Responsibilities:
        1.  List of Vectors in order of discovery on a line.
        2.  Resource for a GraphFactory needs for creating Edge and Node products.

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
    
        
    
        