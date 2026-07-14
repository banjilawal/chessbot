# src/ray/quadrant/ray.py

"""
Module: ray.quadrant.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, cast

from model import Coord, Vector
from ray import Ray
from space import Quadrant


class QuadrantRay(Ray):
    
    _space: Quadrant
    
    def __init(self, space: Quadrant):
        self._space = space
        
    @property
    def space(self) -> Quadrant:
        return cast(Quadrant, self.space)
    
    def vector_ray(self) -> List[Vector]:
        cursor = Vector(
            x=self.space.origin.x,
            y=self._f_of_x(x=self.space.origin.x, slope=self.space.slope)
        )
        terminus = self.space.terminus
        vectors: List[Vector] = []
        
        while cursor != terminus:
            vectors.append(cursor)
            cursor = Vector(
                x=cursor.x,
                y=self._f_of_x(x=cursor.x, slope=self.space.slope)
            )
        return vectors
    
    def coord_ray(self) -> List[Coord]:
        coords: List[Coord] = []
        for vector in self.vector_ray():
            coords.append(Coord(column=vector.x, row=vector.y))
        return coords
    
    def _f_of_x(self, x: int, slope: int) -> int:
        """
        Action:
            Calculate the y component of a vector using the line's
                *   slope
                *   its x component
        Args:
            x: int
            slope: int
        Returns:
            int
        Raises:
            None
        """
        return (2 * slope * x) + slope