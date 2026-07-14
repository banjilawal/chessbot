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
        
    @@property
    def space(self) -> Quadrant:
        return cast(Quadrant, self.space)
    
    def vector_ray(self) -> List[Vector]:
        pass
    
    def coord_ray(self) -> List[Coord]:
        pass