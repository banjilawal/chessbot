# src/ray/axis/ray.py

"""
Module: ray.axis.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, cast


from geometry import Axis
from model import Coord, Vector
from ray import Ray


class AxisRay(Ray):
   
    
    def __init__(self, basis: Axis):
        super().__init__(basis=basis)
        
    @property
    def basis(self) -> Axis:
        return cast(Axis, self.basis)
    
    
    def vector_ray(self,) -> List[Vector]:
        cursor = self.basis.delta_bound.origin
        terminus = self.basis.delta_bound.terminus
        vectors: List[Vector] = []
        
        while cursor != terminus:
            vectors.append(cursor)
            cursor = Vector(
                x=self.basis.delta_bound.delta.x + cursor.x,
                y=self.basis.delta_bound.delta.y + cursor.y
            )
        return vectors
        
    def coord_ray(self) -> List[Coord]:
        coords: List[Coord] = []
        for vector in self.vector_ray():
            coords.append(Coord(column=vector.x, row=vector.y))
        return coords