# src/ray/ray.py

"""
Module: ray.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from model import Coord, Vector
from result import ComputationResult
from toolkit import MathToolkit

T = TypeVar("T", bound= "Space")


class RayComputer(ABC, Generic[T]):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Produce a ray of Vectors from an origin to a terminus.

    Attributes:
        space: T
        math_toolkit: MathToolkit

    Provides:
        -   def vector_ray() -> ComputationResult[List[Vector]]
        -   def coord_ray(self) -> ComputationResult[List[Coord]]

    Super Class:
    """
    _space: T
    _math_toolkit: MathToolkit
    
    def __init__(self, space: T, math_toolkit: MathToolkit | None = MathToolkit()):
        """
        Args:
            space: T
            math_toolkit: MathToolkit
        """
        self._space = space
        self._math_toolkit = math_toolkit
        
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
        
    @property
    def space(self) -> T:
        return self._space
    
    @abstractmethod
    def vector_ray(self,) -> ComputationResult[List[Vector]]:
        pass
    
    @abstractmethod
    def coord_ray(self) -> ComputationResult[List[Coord]]:
        pass