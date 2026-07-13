# src/ray/axis/ray.py

"""
Module: ray.axis.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import List

from bounds import AxisBounds
from model import Coord, Vector
from ray import Ray


class AxisRay(Ray):
    _bounds: AxisBounds
    
    def __init__(self, coord: Coord):
        self._bounds = AxisBounds()
    
    @abstractmethod
    def compute(self, coord) -> List[Vector]:
        pass
    
    def compute(self) -> List[Vector]:
        cursor = self._axis.origin
        vectors: List[Vector] = []
        
        while cursor != self._terminus:
            vectors.append(cursor)
            cursor = Vector(
                x=self._axis.delta.x + cursor.x,
                y=self._axis.delta.y + cursor.y
            )
        return vectors