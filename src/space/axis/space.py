# src/space/axis/space.py

"""
Module: space.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from model import Vector
from result import ComputationResult
from space import AxisBounds, AxisStepper, Space, SpaceBounds
from util import LoggingLevelRouter


class Axis(Space):
    """
    Role:
        -   Addressing
        -   Data-Holder

    Responsibilities:
        1.  Defines the delta_x/delta_y and bounds of an axis relative to a
            token's position.

    Attributes:
        bounds: AxisBounds
        stepper: AxisStepper

    Provides:
        -   next(self, current: Vector) -> ComputationResult
        -   north_axis(cls, origin: Vector) -> Axis
        -   east_axis(cls, origin: Vector) -> Axis
        -   south_axis(cls, origin: Vector) -> Axis
        -   west_axis(cls, origin: Vector) -> Axis
        
    Super Class:
        Space
    """
    _bounds: AxisBounds
    _stepper: AxisStepper

    
    def __init__(
            self,
            bounds: AxisBounds,
            stepper: AxisStepper,
    ):
        """
        Args:
            bounds: AxisBounds
            stepper: AxisStepper
        """
        super().__init__(bounds=bounds)
        self._steeper = stepper
        self._bounds = bounds
        
    @property
    def bounds(self) -> SpaceBounds:
        return cast(AxisBounds, self.bounds)
    
    @property
    def origin(self) -> Vector:
        return self.bounds.origin
    
    @property
    def terminus(self) -> Vector:
        return self.bounds.terminus
    
    @LoggingLevelRouter.monitor
    def next(self, current: Vector) -> ComputationResult:
        method = f"{self.__class__.__name__}.next"
        
        computation = self._stepper.next(u=current)
        if computation.is_failure:
            return ComputationResult.failure(
                computation.exception
            )
        return computation

    
    @classmethod
    def east_axis(cls, origin: Vector) -> Axis:
        return cls(
            stepper=AxisStepper.east(),
            bounds=AxisBounds.east(origin=origin),
        )
    
    @classmethod
    def north_axis(cls, origin: Vector) -> Axis:
        return cls(
            stepper=AxisStepper.east(),
            bounds=AxisBounds.north(origin=origin)
        )
    
    @classmethod
    def south_axis(cls, origin: Vector) -> Axis:
        return cls(
            stepper=AxisStepper.east(),
            bounds=AxisBounds.south(origin=origin)
        )
    
    @classmethod
    def west_axis(cls, origin: Vector) -> Axis:
        return cls(
            stepper=AxisStepper.west(),
            bounds=AxisBounds.west(origin=origin)
        )
    