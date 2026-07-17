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
from space import LinearStepper, Space, LinearSection
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
    _section: LinearSection
    _stepper: LinearStepper

    _math_toolkit: Optional[MathToolkit]
    
    def __init__(
            self,
            linear_section: LinearSection,
            stepper: LinearStepper,
            validator: LinearSectionValidator,
            math_toolkit: Optional[MathToolkit] | None = MathToolkit(),
    ):
        """
        Args:
            linear_section: SpaceBounds
            stepper: Stepper
            validator: Validator
            math_toolkit: Optional[MathToolkit]
        """
        self._section = linear_section
        self._stepper = stepper
        self._validator = validator
        self._math_toolkit = math_toolkit
    
    @property
    def bounds(self) -> LinearSection:
        return self._section
    
    @property
    def stepper(self) -> LinearStepper:
        return self._stepper
    
    @property
    def validator(self) -> Validator:
        return self._validator
    
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    
    @property
    def is_empty(self) -> bool:
        return self._section.is_empty
    
    @property
    def is_cycle(self) -> bool:
        return self._section.is_cycle
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def distance(self) -> ComputationResult[Scalar]:
        pass