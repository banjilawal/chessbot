# src/space/linear/linear.py

"""
Module: space.linear.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Optional

from model import Scalar
from result import ComputationResult
from space import LinearStepper, Space, LinearBounds
from toolkit import MathToolkit
from util import LoggingLevelRouter
from validator import Validator


class LinearSpace(Space):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define points in a bounded space.
        2.  Provide a function that steps through every point in the plane,

    Attributes:
        bounds: SpaceBounds
        stepper: Stepper
        math_toolkit: Optional[MathToolkit]

    Provides:

    Super Class:
    """
    _bounds: LinearBounds
    _stepper: LinearStepper
    _validator: Validator[T]
    _math_toolkit: Optional[MathToolkit]
    
    def __init__(
            self,
            bounds: LinearBounds,
            stepper: LinearStepper,
            validator: Validator[T],
            math_toolkit: Optional[MathToolkit] | None = MathToolkit(),
    ):
        """
        Args:
            bounds: SpaceBounds
            stepper: Stepper
            validator: Validator
            math_toolkit: Optional[MathToolkit]
        """
        self._bounds = bounds
        self._stepper = stepper
        self._validator = validator
        self._math_toolkit = math_toolkit
    
    @property
    def bounds(self) -> LinearBounds:
        return self._bounds
    
    @property
    def stepper(self) -> LinearStepper:
        return self._stepper
    
    @property
    def validator(self) -> Validator[T]:
        return self._validator
    
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    
    @property
    def is_empty(self) -> bool:
        return self._bounds.is_empty
    
    @property
    def is_cycle(self) -> bool:
        return self._bounds.is_cycle
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def distance(self) -> ComputationResult[Scalar]:
        pass