# src/model/ray/coord/model.py

"""
Module: model.ray.coord.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Iterator, Optional, cast

from model import Coord, Ray, Vector


class CoordRay(Ray[Coord]):
    
    def __init__(self, origin: Coord):
        """
        Args:
            origin: Coord
        """
        super().__init__(origin=origin)
    
    @property
    def origin(self) -> Optional[Coord]:
        return cast(Coord, self._points[0])
    
    @property
    def terminus(self) -> Optional[Coord]:
        return cast(Coord, self._points[-1])
    
    @property
    def iterator(self) -> Iterator[Coord]:
        return iter(self._points)
    
    @property
    def is_cycle(self) -> bool:
        return super().is_cycle and self.origin == self.terminus
    
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
    
        
    
        