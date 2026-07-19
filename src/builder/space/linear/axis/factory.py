# src/space/linear/axis/space.py

"""
Module: space.linear.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, cast

from builder import Builder
from err import AxisException
from model import Scalar, Vector
from register import VectorRegister
from result import BuildResult, ComputationResult, MethodResultType
from schema import AxisOrientation
from space import Axis, AxisEndpointFactory, AxisStepper, LinearSpace, LinearTargetSet, TargetSpanSet
from util import LoggingLevelRouter


class AxisSpaceFactory(Builder[Axis]):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define a set of Vectors from an origin..
        2.  Provide the next point in the direction of travel.

    Attributes:
        origin: Vector
        stepper: AxisStepper
        orientation: AxisOrientation
        
        east_axis_builder: Optional[EastAxisBuilder]
        north_axis_builder: Optional[NorthAxisBuilder]
        south_axis_builder: Optional[SouthAxisBuilder]
        west_axis_builder: Optional[WestAxisBuilder]
        axis_endpoint_factory: Optional[AxisEndpointFactory]
        
    Provides:
        -   def execute(self) -> BuildResult[Axis]

    Super Class:
        LinearSpaceFactory
    """
    _orientation: Vector
    _endpoints: VectorRegister
    _stepper: AxisStepper
    _orientation: AxisOrientation
    
    _east_axis_builder: EastAxisBuilder
    _north_axis_builder: NorthAxisBuilder
    _south_axis_builder: SouthAxisBuilder
    _west_axis_builder: WestAxisBuilder
    
    _axis_endpoint_factory: AxisEndpointFactory
    
    def __init__(
            self,
            origin: Vector,
            endpoints: VectorRegister,
            stepper: AxisStepper,
            orientation: AxisOrientation,
            
            east_axis_builder: Optional[EastAxisBuilder] | None = EastAxisBuilder(),
            north_axis_builder: Optional[NorthAxisBuilder] | None = NorthAxisBuilder(),
            south_axis_builder: Optional[SouthAxisBuilder] | None = SouthAxisBuilder(),
            west_axis_builder: Optional[WestAxisBuilder] | None = WestAxisBuilder(),
            axis_endpoint_factory: Optional[AxisEndpointFactory] | None = AxisEndpointFactory()
    ):
        """
        Args:
            endpoints: AxisLinear_Section
            stepper: AxisStepper
            orientation: AxisOrientation
            
            east_axis_builder: Optional[EastAxisBuilder]
            north_axis_builder: Optional[NorthAxisBuilder]
            south_axis_builder: Optional[SouthAxisBuilder]
            west_axis_builder: Optional[WestAxisBuilder]
            axis_endpoint_factory: Optional[AxisEndpointFactory]
        """
        super().__init__(endpoints=endpoints, stepper=stepper)
        self._endpoints = endpoints
        self._stepper = stepper
        self._orientation = orientation
        self._origin = origin
        
    @property
    def orientation(self) ->AxisOrientation:
        return self._orientation
    
    @property
    def stepper(self) -> AxisStepper:
        return self._stepper
    
    @property
    def endpoints(self) -> VectorRegister:
        return self._endpoints
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[Axis]:
        
        request: BuildResult
        if self.orientation == AxisOrientation.NORTH:
            request = NorthAxisBuilder.execute(origin=self._origin)
        if self.orientation == AxisOrientation.SOUTH:
            request = SouthAxisBuilder.execute(origin=self._origin)
        if self.orientation == AxisOrientation.EAST:
            request = EastAxisBuilder.execute(origin=self._origin)
        if self.orientation == AxisOrientation.WEST:
            request = WestAxisBuilder.execute(origin=self._origin)
            
        if request.is_failure:
            return BuildResult.failure(
                AxisSpaceFactoryException(
                    cls_mth=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisSpaceFactoryException.MSG,
                    err_code=AxisSpaceFactoryException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=request.exception
                )
            )
        return BuildResult.success(
            cast(Axis, request.payload)
        )

    
    @classmethod
    def east_axis(cls, origin: Vector) -> Axis:
        """
        Create an Axis in 1D plane
        
        Linear_Section:
        
            east => [u, Vector(num_columns - 1, u.y)], (i, 0)
        Delta:
            d_x => increments u.x by 1 till x = num_columns - 1
            d_y => 0
        """
        return cls(
            stepper=AxisStepper.east(),
            endpoints=AxisEndpointFactory.east(origin=origin),
        )
    
    @classmethod
    def north_axis(cls, origin: Vector) -> Axis:
        """
        Create an Axis in 1D plane.

        Linear_Section:
            north => [u, Vector(u.x, 0)], (0, -j)
        Delta:
            d_x => 0
            d_y => increments u.y by -1 till y = 0
        """
        return cls(
            stepper=AxisStepper.east(),
            endpoints=AxisEndpointFactory.north(origin=origin)
        )
    
    @classmethod
    def south_axis(cls, origin: Vector) -> Axis:
        """
        Create an Axis in 1D plane.

        Linear_Section:
            south => [u, Vector(u.x, num_rows - 1)], (0, j)
        Delta:
            d_x => 0
            d_y => increments u.y by 1 till y = num_rows - 1
        """
        return cls(
            stepper=AxisStepper.east(),
            endpoints=AxisEndpointFactory.south(origin=origin)
        )
    
    @classmethod
    def west_axis(cls, origin: Vector) -> Axis:
        """
        Create an Axis in 1D plane.

        Linear_Section:
            west => [u, Vector(0, u.y)], (-i, 0)
        Delta:
            d_x => increments u.x by -1 till x = 0
            d_y => 0
        """
        return cls(
            stepper=AxisStepper.west(),
            endpoints=AxisEndpointFactory.west(origin=origin)
        )
    