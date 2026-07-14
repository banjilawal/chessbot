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
from space import Space
from toolkit import MathToolkit


class RayComputer:
    _space: Space
    _math: MathToolkit
    
    def __init__(self, space: Space, math: MathToolkit | None = MathToolkit()):
        self._space = space
        self._math = math
        
    @property
    def math(self) -> MathToolkit:
        return self._math
        
    @property
    def space(self) -> Space:
        return self._space
    
    @abstractmethod
    def vector_ray(self,) -> List[Vector]:
        pass
    
    @abstractmethod
    def coord_ray(self) -> List[Coord]:
        pass