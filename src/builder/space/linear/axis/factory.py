# src/space/linear/axis/space.py

"""
Module: space.linear.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from builder import Builder, EastAxisBuilder, NorthAxisBuilder, SouthAxisBuilder, WestAxisBuilder
from factory import AxisEndpointFactory
from model import Vector
from register import VectorRegister
from result import BuildResult
from schema import AxisOrientation
from space import Axis, AxisStepper
from toggle import OrientationToggle
from util import LoggingLevelRouter
from validator import VectorValidator


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
        toggle: OrientationToggle
        
    Provides:
        -   def execute(self) -> BuildResult[Axis]

    Super Class:
        LinearSpaceFactory
    """
    _orientation: Vector
    _stepper: AxisStepper
    _toggle: OrientationToggle
    _vector_validator: Optional[VectorValidator]
    
    def __init__(
            self,
            origin: Vector,
            stepper: AxisStepper,
            toggle: OrientationToggle,
            vector_validator: Optional[VectorValidator] | None = VectorValidator(),
    ):
        """
        Args:
            endpoints: AxisLinear_Section
            stepper: AxisStepper
            toggle: OrientationToggle
            vector_validator: Optional[VectorValidator]
        """
        self._stepper = stepper
        self._toggle = toggle
        self._origin = origin
        self._vector_validator = vector_validator
        
    @property
    def toggle(self) -> OrientationToggle:
        return self._toggle
    
    @property
    def stepper(self) -> AxisStepper:
        return self._stepper
    
    @property
    def vector_validator(self) -> VectorValidator:
        return self._vector_validator
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[Axis]:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that. the origin is flagged unsafe.
        validation = self._vector_validator.execute(self._origin)
        if validation.is_failure:
            # Send the exception chain in the result.
            return BuildResult.failure(
                AxisSpaceFactoryException(
                    cls_mth=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisSpaceFactoryException.MSG,
                    err_code=AxisSpaceFactoryException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=WrongToggleException(
                        cls_mth=method,
                        cls_name=self.__class__.__name__,
                        msg=AxisSpaceFactoryException.MSG,
                        err_code=AxisSpaceFactoryException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    )
                )
            )
        origin = cast(Vector, validation.payload
                      )
        # Handle the case that, the orientation is toggled for a quadrant.
        if not self._toggle.is_axis_toggle:
            # Send the exception chain in the result.
            return BuildResult.failure(
                AxisSpaceFactoryException(
                    cls_mth=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisSpaceFactoryException.MSG,
                    err_code=AxisSpaceFactoryException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=WrongToggleException(
                        cls_mth=method,
                        cls_name=self.__class__.__name__,
                        msg=AxisSpaceFactoryException.MSG,
                        err_code=AxisSpaceFactoryException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    )
                )
            )
        request: BuildResult = BuildResult.failure()
        
        # Route to the appropriate AxisBuilder.
        if self._toggle.entity == AxisOrientation.NORTH:
            request = NorthAxisBuilder.execute(
                origin=origin
            )
        if self._toggle.entity == AxisOrientation.SOUTH:
            request = SouthAxisBuilder.execute(
                origin=origin
            )
        if self._toggle.entity == AxisOrientation.EAST:
            request = EastAxisBuilder.execute(
                origin=origin
            )
        if self._toggle.entity == AxisOrientation.WEST:
            request = WestAxisBuilder.execute(
                origin=origin
            )
         
        # Handle the case that, the request is not fulfilled.
        if request.is_failure:
            # Send the exception chain in the result.
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
        return BuildResult.success(cast(Axis, request.payload))
    