# src/space/ray/computer/space/ray.py

"""
Module: space.ray.computer.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from space.destination import SpanVectorSet
from model import Vector
from result import ComputationResult
from toolkit import MathToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound= "Space")


class LinearJoiner(ABC, Generic[T]):
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
    _linear_space: T
    _math_toolkit: MathToolkit
    
    def __init__(
            self,
            linear_space: T,
            math_toolkit: MathToolkit | None = MathToolkit()
    ):
        """
        Args:
            linear_space: T
            math_toolkit: MathToolkit
        """
        self._linear_space = linear_space
        self._math_toolkit = math_toolkit
        
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
        
    @property
    def linear_space(self) -> T:
        return self._linear_space
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, origin: Vector) -> ComputationResult[SpanVectorSet]:
        pass