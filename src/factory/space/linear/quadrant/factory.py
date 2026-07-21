# src/space/linear/quadrant/space.py

"""
Module: space.linear.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from builder import Builder, EastQuadrantBuilder, NortheastQuadrantBuilder, SoutheastQuadrantBuilder, WestQuadrantBuilder
from model import Vector
from result import BuildResult
from schema import QuadrantOrientation
from space import Quadrant, QuadrantStepper
from toggle import OrientationToggle
from util import LoggingLevelRouter
from validator import VectorValidator


class QuadrantSpaceFactory(Builder[Quadrant]):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define a set of Vectors from an origin..
        2.  Provide the next point in the direction of travel.

    Attributes:
        origin: Vector
        stepper: QuadrantStepper
        toggle: OrientationToggle
        
    Provides:
        -   def execute(self) -> BuildResult[Quadrant]

    Super Class:
        LinearSpaceFactory
    """
    _orientation: Vector
    _stepper: QuadrantStepper
    _toggle: OrientationToggle
    _vector_validator: Optional[VectorValidator]
    
    def __init__(
            self,
            origin: Vector,
            stepper: QuadrantStepper,
            toggle: OrientationToggle,
            vector_validator: Optional[VectorValidator] | None = VectorValidator(),
    ):
        """
        Args:
            endpoints: QuadrantLinear_Section
            stepper: QuadrantStepper
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
    def stepper(self) -> QuadrantStepper:
        return self._stepper
    
    @property
    def vector_validator(self) -> VectorValidator:
        return self._vector_validator
    
    @LoggingLevelRouter.monitor
    def execute(self,
            origin: Vector,
            toggle: OrientationToggle,
    ) -> BuildResult[Quadrant]:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that. the origin is flagged unsafe.
        validation = self._vector_validator.execute(self._origin)
        if validation.is_failure:
            # Send the exception chain in the result.
            return BuildResult.failure(
                QuadrantSpaceFactoryException(
                    cls_mth=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantSpaceFactoryException.MSG,
                    err_code=QuadrantSpaceFactoryException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=WrongToggleException(
                        cls_mth=method,
                        cls_name=self.__class__.__name__,
                        msg=QuadrantSpaceFactoryException.MSG,
                        err_code=QuadrantSpaceFactoryException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    )
                )
            )
        origin = cast(Vector, validation.payload
                      )
        # Handle the case that, the orientation is toggled for a quadrant.
        if not self._toggle.is_quadrant_toggle:
            # Send the exception chain in the result.
            return BuildResult.failure(
                QuadrantSpaceFactoryException(
                    cls_mth=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantSpaceFactoryException.MSG,
                    err_code=QuadrantSpaceFactoryException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=WrongToggleException(
                        cls_mth=method,
                        cls_name=self.__class__.__name__,
                        msg=QuadrantSpaceFactoryException.MSG,
                        err_code=QuadrantSpaceFactoryException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    )
                )
            )
        request: BuildResult = BuildResult.failure()
        
        # Route to the appropriate QuadrantBuilder.
        if self._toggle.entity == QuadrantOrientation.NORTHEAST:
            request = NortheastQuadrantBuilder.execute(
                origin=origin
            )
        if self._toggle.entity == QuadrantOrientation.SOUTHEAST:
            request = SoutheastQuadrantBuilder.execute(
                origin=origin
            )
        if self._toggle.entity == QuadrantOrientation.NORTHEAST:
            request = NortheastQuadrantBuilder.execute(
                origin=origin
            )
        if self._toggle.entity == QuadrantOrientation.NORTHWEST:
            request = NorthwestQuadrantBuilder.execute(
                origin=origin
            )
         
        # Handle the case that, the request is not fulfilled.
        if request.is_failure:
            # Send the exception chain in the result.
            return BuildResult.failure(
                QuadrantSpaceFactoryException(
                    cls_mth=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantSpaceFactoryException.MSG,
                    err_code=QuadrantSpaceFactoryException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=request.exception
                )
            )
        return BuildResult.success(cast(Quadrant, request.payload))
    