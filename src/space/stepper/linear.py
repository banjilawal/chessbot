# src/space/stepper/linear.py

"""
Module: space.stepper.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from model import Vector
from result import ComputationResult
from toolkit import MathToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="LinearSpace")


class LinearStepper(ABC, Generic[T]):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Get the next Vector that exists in the direction of travel

    Attributes:
        math: MathToolkit

    Provides:
        -   def next(current: Vector) -> ComputationResult[Vector]:

    Super Class:
    """
    _math_toolkit: MathToolkit
    
    def __init__(
            self,
            math_toolkit: MathToolkit | None = MathToolkit(),
    ):
        """
        Args
            math_toolkit: MathToolkit
        """
        self._math_toolkit = math_toolkit
        
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def next(self, current: Vector) -> ComputationResult[Vector]:
        pass