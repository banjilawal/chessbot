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
from space import LinearStepper, Space, LineSegment
from toolkit import MathToolkit
from util import LoggingLevelRouter



class LinearSpace(Space):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define points in a bounded space.
        2.  Provide a function that steps through every point in the plane,

    Attributes:
        segment: LineSegment
        stepper: LinearStepper
        math_toolkit: Optional[MathToolkit]

    Provides:

    Super Class:
    """
    _segment: LineSegment
    _stepper: LinearStepper
    _math_toolkit: Optional[MathToolkit]
    
    def __init__(
            self,
            segment: LineSegment,
            stepper: LinearStepper,
            math_toolkit: Optional[MathToolkit] | None = MathToolkit(),
    ):
        """
        Args:
            segment: LineSegment
            stepper: Stepper
            validator: Validator
            math_toolkit: Optional[MathToolkit]
        """
        self._segment = segment
        self._stepper = stepper
        self._math_toolkit = math_toolkit
    
    @property
    def segment(self) -> LineSegment:
        return self._segment
    
    @property
    def stepper(self) -> LinearStepper:
        return self._stepper
    
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    
    @property
    def is_empty(self) -> bool:
        return self._segment.is_empty
    
    @property
    def is_cycle(self) -> bool:
        return self._segment.is_cycle
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def distance(self) -> ComputationResult[Scalar]:
        pass