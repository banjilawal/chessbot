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

from container import SpanVectorSet
from model import Vector
from space import LinearSpace
from result import ComputationResult
from toolkit import MathToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound= "LinearSpace")


class LinearSpanTransformer(ABC, Generic[T]):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Produce a ray of Vectors from an origin to a terminus.

    Attributes:
        space: T
        math_toolkit: MathToolkit

    Provides:
        -   def execute() -> ComputationResult[SpanVectorSet]
        
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
    def execute(self,) -> ComputationResult[SpanVectorSet]:
        pass