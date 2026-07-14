# src/ray/axis/ray.py

"""
Module: ray.axis.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, cast


from model import Coord, Vector
from ray import Ray
from space import Axis


class AxisRay(Ray):
   
    
    def __init__(self, space: Axis):
        super().__init__(space=space)
        
    @property
    def space(self) -> Axis:
        return cast(Axis, self.space)
    
    
    def vector_ray(self,) -> List[Vector]:
        cursor = self.space.delta_bound.origin
        terminus = self.space.delta_bound.terminus
        vectors: List[Vector] = []
        
        while cursor != terminus:
            vectors.append(cursor)
            cursor = Vector(
                x=self.space.delta_bound.delta.x + cursor.x,
                y=self.space.delta_bound.delta.y + cursor.y
            )
        return vectors
        
    def coord_ray(self) -> List[Coord]:
        coords: List[Coord] = []
        for vector in self.vector_ray():
            coords.append(Coord(column=vector.x, row=vector.y))
        return coords