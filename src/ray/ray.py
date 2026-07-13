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

from model import Coord, Vector


class Ray:
    
    @abstractmethod
    def vector_ray(self,) -> List[Vector]:
        pass
    
    @abstractmethod
    def coord_ray(self) -> List[Coord]:
        pass