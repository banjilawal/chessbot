# src/ray/ray.py

"""
Module: ray.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import List

from bounds import RayBounds
from model import Coord, Vector


class Ray:
    _bounds: RayBounds
    
    def __init__(self, bounds: RayBounds):
        self._bounds = bounds
        
    @property
    def bounds(self) -> RayBounds:
        return self._bounds
    
    @abstractmethod
    def vector_ray(self,) -> List[Vector]:
        pass
    
    @abstractmethod
    def coord_ray(self) -> List[Coord]:
        pass