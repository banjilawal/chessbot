# src/ray/axis/ray.py

"""
Module: ray.axis.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from bounds import AxisBounds
from model import Coord, Vector
from ray import Ray


class AxisRay(Ray):
    _bounds: AxisBounds
    
    def __init__(self, coord: Coord):
        self._bounds = AxisBounds()
    
    
    def vector_ray(self,) -> List[Vector]:
        cursor = self._bounds.axis.origin
        vectors: List[Vector] = []
        
        while cursor != self._bounds.terminus:
            vectors.append(cursor)
            cursor = Vector(
                x=self._bounds.axis.delta.x + cursor.x,
                y=self._bounds.axis.delta.y + cursor.y
            )
            return vectors
        
    def coord_ray(self) -> List[Coord]:
        coords: List[Coord] = []
        for vector in self.vector_ray():
            coords.append(Coord(column=vector.x, row=vector.y))
        return coords