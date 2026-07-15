# src/space/axis/space.py

"""
Module: space.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from err import AxisSpaceException
from model import Scalar, Vector
from register import VectorRegister
from result import ComputationResult, MethodResultType
from space import AxisBounds, AxisStepper, Space, SpaceBounds
from util import LoggingLevelRouter


class Axis(Space):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define a set of Vectors from an origin..
        2.  Provide the next point in the direction of travel.

    Attributes:
        bounds: AxisBounds
        stepper: AxisStepper

    Provides:
        -   def next(current: Vector) -> ComputationResult
        -   def northeast(origin: Vector) -> Axis
        -   def northwest(origin: Vector) -> Axis
        -   def southeast(origin: Vector) -> Axis
        -   def southwest(origin: Vector) -> Axis

    Super Class:
        Space

    WARNING:
        *****===ONLY_INSTANTIATE_WITH_THE_FACTORY_METHODS===*****
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
        super().__init__(bounds=bounds, stepper=stepper)
    """INTERNAL: Use factory methods instead of direct constructor."""
    
    @property
    def bounds(self) -> AxisBounds:
        return cast(AxisBounds, self.bounds)
    
    @property
    def stepper(self) -> AxisStepper:
        return cast(AxisStepper, self.stepper)
    
    @property
    def origin(self) -> Vector:
        return self.bounds.origin
    
    @property
    def terminus(self) -> Vector:
        return self.bounds.terminus
    
    @LoggingLevelRouter.monitor
    def distance(self) -> ComputationResult[Scalar]:
        """
        Get the Euclidean distance between the Space's endpoints.

        Action:
            1.  Send an exception chain in the ComputationResult if the math toolkit
                cannot produce a solution.
            2.  Otherwise, send the computed vector in the success result.
        Args:
        Returns:
            ComputationResult[Scalar]
        Raises:
             AxisSpaceException
        """
        method = f"{self.__class__.__name__}.distance"
        
        # Request the Euclidean distance
        computation = self.math.euclidean_distance.execute(
            register=VectorRegister(u=self.origin, v=self.terminus)
        )
        # Handle the case that, the computation is not satisfied.
        if computation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                AxisSpaceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisSpaceException.MSG,
                    err_code=AxisSpaceException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=computation.exception,
                ),
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(cast(Scalar, computation.payload))
    
    
    @LoggingLevelRouter.monitor
    def next(self, current: Vector) -> ComputationResult[Vector]:
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
             AxisSpaceException
        """
        method = f"{self.__class__.__name__}.next"
        
        # --- Request the next Vector for the stepper. ---#
        computation = self._stepper.next(u=current)
        
        # Handle the case that, the computation is aborted.
        if computation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                AxisSpaceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisSpaceException.MSG,
                    err_code=AxisSpaceException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=computation.exception,
                ),
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(cast(Vector, computation.payload))

    
    @classmethod
    def east_axis(cls, origin: Vector) -> Axis:
        """
        Create an Axis in 1D plane
        
        Bounds:
        
            east => [u, Vector(num_columns - 1, u.y)], (i, 0)
        Delta:
            d_x => increments u.x by 1 till x = num_columns - 1
            d_y => 0
        """
        return cls(
            stepper=AxisStepper.east(),
            bounds=AxisBounds.east(origin=origin),
        )
    
    @classmethod
    def north_axis(cls, origin: Vector) -> Axis:
        """
        Create an Axis in 1D plane.

        Bounds:
            north => [u, Vector(u.x, 0)], (0, -j)
        Delta:
            d_x => 0
            d_y => increments u.y by -1 till y = 0
        """
        return cls(
            stepper=AxisStepper.east(),
            bounds=AxisBounds.north(origin=origin)
        )
    
    @classmethod
    def south_axis(cls, origin: Vector) -> Axis:
        """
        Create an Axis in 1D plane.

        Bounds:
            south => [u, Vector(u.x, num_rows - 1)], (0, j)
        Delta:
            d_x => 0
            d_y => increments u.y by 1 till y = num_rows - 1
        """
        return cls(
            stepper=AxisStepper.east(),
            bounds=AxisBounds.south(origin=origin)
        )
    
    @classmethod
    def west_axis(cls, origin: Vector) -> Axis:
        """
        Create an Axis in 1D plane.

        Bounds:
            west => [u, Vector(0, u.y)], (-i, 0)
        Delta:
            d_x => increments u.x by -1 till x = 0
            d_y => 0
        """
        return cls(
            stepper=AxisStepper.west(),
            bounds=AxisBounds.west(origin=origin)
        )
    