# src/space/quadrant/space.py

"""
Module: space.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from pickletools import uint1
from typing import cast

from model import Vector
from result import ComputationResult
from space import QuadrantBounds, QuadrantStepper, Space
from util import LoggingLevelRouter


class Quadrant(Space):
    """
    Role:
        -   Addressing
        -   Data-Holder

    Responsibilities:
        1.  Defines the delta_x/delta_y and bounds of a quadrant relative to a
            token's position.

    Attributes:
        bounds: QuadrantBounds
        stepper: QuadrantStepper

    Provides:

    Super Class:
        Space
    """
    _bounds: QuadrantBounds
    _stepper: QuadrantStepper
    
    def __init__(self, stepper: QuadrantStepper, bounds: QuadrantBounds):
        """
        Args:
            bounds: QuadrantBounds
            stepper: QuadrantStepper
        """
        super().__init__(bounds=bounds)
        """INTERNAL: Use factory methods instead of direct constructor."""
        self._stepper = stepper
        
    @property
    def bounds(self) -> QuadrantBounds:
        return cast(QuadrantBounds, self.bounds)
    
    @property
    def origin(self) -> Vector:
        return self.bounds.origin
    
    @property
    def terminus(self) -> Vector:
        return self.bounds.terminus
    
    @LoggingLevelRouter.monitor
    def next(self, current: Vector) -> ComputationResult:
        method = f"{self.__class__.__name__}"
        
        result = self._stepper.next(current=current)
        if result.is_failure:
            return ComputationResult.failure(
                result.exception
            )
        return result
        
    
    @classmethod
    def northeast(cls, origin: Vector) -> Quadrant:
        return cls(
            stepper=QuadrantStepper.northeast(),
            bounds=QuadrantBounds.northeast(origin=origin)
        )
    
    @classmethod
    def northwest(cls, origin: Vector) -> Quadrant:
        return cls(
            stepper=QuadrantStepper.northwest(),
            bounds=QuadrantBounds.northwest(origin=origin)
        )
    
    @classmethod
    def southeast(cls, origin: Vector) -> Quadrant:
        return cls(
            stepper=QuadrantStepper.southeast(),
            bounds=QuadrantBounds.southeast(origin=origin)
        )
    
    @classmethod
    def southwest(cls, origin: Vector) -> Quadrant:
        return cls(
            stepper=QuadrantStepper.southwest(),
            bounds=QuadrantBounds.southwest(origin=origin)
        )
        
    