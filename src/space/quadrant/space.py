# src/space/quadrant/space.py

"""
Module: space.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from err import QuadrantSpaceException
from model import Vector
from result import ComputationResult, MethodResultType
from space import QuadrantBounds, QuadrantStepper, Space
from util import LoggingLevelRouter


class Quadrant(Space):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define a bounded 2D space.
        2.  Provide Provide the next point in the direction of of travel.

    Attributes:
        bounds: QuadrantBounds
        stepper: QuadrantStepper

    Provides:
        -   def next(current: Vector) -> ComputationResult
        -   def northeast(origin: Vector) -> Quadrant
        -   def northwest(origin: Vector) -> Quadrant
        -   def southeast(origin: Vector) -> Quadrant
        -   def southwest(origin: Vector) -> Quadrant

    Super Class:
        Space

    WARNING:
        *****===ONLY_INSTANTIATE_WITH_THE_FACTORY_METHODS===*****
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
        """
        Get the next vector in the direction of travel.

        Action:
            1.  Send an exception chain in the ComputationResult if the stepper aborts.
            2.  Otherwise, send the computed vector in the success result.
        Args:
            current: Vector
        Returns:
            ComputationResult[Vector]
        Raises:
             QuadrantSpaceException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Request the next Vector for the stepper. ---#
        computation = self._stepper.next(current=current)
        
        # Handle the case that, the computation is aborted.
        if computation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                QuadrantSpaceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantSpaceException.MSG,
                    err_code=QuadrantSpaceException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=computation.exception,
                ),
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(cast(Vector, computation.payload))

    @classmethod
    def northeast(cls, origin: Vector) -> Quadrant:
        """
        Create a 2D space

        Bounds:
            northeast => [u, Vector(num_columns - 1, 0)], (i, 0)
        Functions:
            f(x) = x + 1
            g(x) = -2x + 1
        """
        return cls(
            stepper=QuadrantStepper.northeast(),
            bounds=QuadrantBounds.northeast(origin=origin)
        )
    
    @classmethod
    def northwest(cls, origin: Vector) -> Quadrant:
        """
        Create a 2D space

        Bounds:
            northwest => [u, Vector(0, 0)], (i, 0)
        Functions:
            f(x) = x - 1
            g(x) = -2x + 1
        """
        return cls(
            stepper=QuadrantStepper.northwest(),
            bounds=QuadrantBounds.northwest(origin=origin)
        )
    
    @classmethod
    def southeast(cls, origin: Vector) -> Quadrant:
        """
        Create a 2D space

        Bounds:
            southeast => [u, Vector(num_columns - 1, num_rows - 1)], (i, 0)
        Functions:
            f(x) = x + 1
            g(x) = 2x + 1
        """
        return cls(
            stepper=QuadrantStepper.southeast(),
            bounds=QuadrantBounds.southeast(origin=origin)
        )
    
    @classmethod
    def southwest(cls, origin: Vector) -> Quadrant:
        """
        Create a 2D space

        Bounds:
            southwest => [u, Vector(0, num_rows - 1)]
        Functions:
            f(x) = x - 1
            g(x) = 2x + 1
        """
        return cls(
            stepper=QuadrantStepper.southwest(),
            bounds=QuadrantBounds.southwest(origin=origin)
        )
        
    