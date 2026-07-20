# src/space/linear/axis/space.py

"""
Module: space.linear.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, cast


from err import AxisException
from model import Scalar, Vector
from register import VectorRegister
from result import ComputationResult, MethodResultType
from space import AxisEndpointFactory, AxisStepper, LinearSpace, LinearTargetSet, TargetSpanSet
from util import LoggingLevelRouter


class Axis(LinearSpace):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define a set of Vectors from an origin..
        2.  Provide the next point in the direction of travel.

    Attributes:
        linear_section: AxisLinear_Section
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
    _endpoints: VectorRegister
    _stepper: AxisStepper
    
    def __init__(self, endpoints: VectorRegister, stepper: AxisStepper,):
        """
        Args:
            endpoints: AxisLinear_Section
            stepper: AxisStepper
        """
        super().__init__(endpoints=endpoints, stepper=stepper)
    
    @property
    def stepper(self) -> AxisStepper:
        return cast(AxisStepper, self.stepper)
    
 

    
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
    