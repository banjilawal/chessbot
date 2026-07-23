# src/stepper/stepper.py

"""
Module: stepper.stepper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from model import Vector
from result import ComputationResult
from toolkit import MathToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Space")


class SpaceStepper(ABC, Generic[T]):
    """
    Role:
        -   Computation

    Responsibilities:
        1.  Stepping function which gives the next vector in a Space.

    Attributes:
        math_toolkit: Optional[MathToolkit

    Provides:
        def next(self, vector: Vector) -> ComputationResult[Vector]

    Super Class:
    """
    
    _math_toolkit: Optional[MathToolkit]
    
    def __init__(self, math_toolkit: Optional[MathToolkit] | None = MathToolkit(),):
        """
        Args:
            math_toolkit: Optional[MathToolkit]
        """
        self._math_toolkit = math_toolkit
    
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def next(self, vector: Vector) -> ComputationResult[Vector]:
        pass
