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


from geometry import Space
from model import Coord, Vector


class Ray:
    _basis: Space
    
    def __init__(self, basis: Space):
        self._basis = basis
        
    @property
    def basis(self) -> Space:
        return self._basis
    
    @abstractmethod
    def vector_ray(self,) -> List[Vector]:
        pass
    
    @abstractmethod
    def coord_ray(self) -> List[Coord]:
        pass