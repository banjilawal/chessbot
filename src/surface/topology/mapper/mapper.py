# src/topology/mapper/mapper.py

"""
Module: topology.mapper.mapper
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from artifcat import ComputationResult
from controller import VectorComputationController
from domain import Vector
from surface import Space
from util import LoggingLevelRouter

T = TypeVar("T", bound="Space")


class SpaceMappingFunction(ABC, Generic[T]):
    """
    Role:
        - Computation

    Responsibilities:
        1.  Stepping function which gives the next vector in a Space.

    Attributes:
        math_toolkit: Optional[MathToolkit

    Provides:
        def next(self, vector: Vector) -> ComputationResult[Vector]

    Super Class:
    """
    _compute: VectorComputationController
    
    
    def __init__(
            self, compute: Optional[VectorComputationController] | None = None,):
        """
        Args:
            compute: Optional[VectorComputationController]
        """
        self._compute = compute or VectorComputationController()
    
    @property
    def compute(self) -> VectorComputationController:
        return self._compute
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def next(self, vector: Vector) -> ComputationResult[Vector]:
        pass
