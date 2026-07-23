# src/stepper/quadrant/stepper.py

"""
Module: stepper.quadrant.stepper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from err import QuadrantStepperException
from model import Vector
from result import ComputationResult, MethodResultType
from stepper import SpaceStepper
from util import LoggingLevelRouter

T = TypeVar("T", bound="QuadrantSpace")

class QuadrantStepper(SpaceStepper, Generic[T]):
    """
    Role:
        -   Computation

    Responsibilities:
        1.  Get the next vector, V, after U in Quadrant Space, using the linear functions:
                -   V.x = U.x + x_step
                -   V.y = (2 * slope * U.y) + slope

    Attributes:
        x_step: int
        slope: int

    Provides:
        def next(self, vector: Vector) -> ComputationResult[Vector]

    Super Class:
        SpaceStepper
    """
    _x_step: int
    _slope: int
    
    def __init__(self, x_step: int, slope: int,):
        """
        Args:
            x_step: int
            slope: int
        """
        super().__init__()
        self._x_step = x_step
        self._slope = slope
        
    @property
    def x_step(self) -> int:
        return self._x_step
    
    @property
    def slope(self) -> int:
        return self._slope
    
    @LoggingLevelRouter.monitor
    def next(self, vector: Vector) -> ComputationResult[Vector]:
        """
        Get the next Vector using a linear function.

        Action:
            1.  Set
                    x_next = x_current + x_step
                    y_next = (2 * slope * y_current) + slope
            2.  If VectorBuilder cannot create a safe Vector from x_next, y_next, send
                an exception chain in the ComputationResult.
            3.  Otherwise, cast the build product, then send in the success result.
        Args:
            vector: Vector
        Returns:
            ComputationResult[Vector]
        Raises:
             QuadrantStepperException
        """
        method = f"{self.__class__.__name__}.next"
        
        # Handle the case that, the argument is not safe to use.
        validation = self.math.vector.validator.execute(vector)
        if validation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                QuadrantStepperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantStepperException.MSG,
                    err_code=QuadrantStepperException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=validation.exception,
                ),
            )
        current = cast(Vector, validation.payload)
        
        # --- Build a new vector from the current. ---#
        build = self.math.vector.builder.execute(
            x=current.x + self._x_step,
            y=(2 * current.y * self._slope) + self.slope
        )
        # Handle the case that, the build is not successful.
        if build.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                QuadrantStepperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantStepperException.MSG,
                    err_code=QuadrantStepperException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=build.exception,
                ),
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(cast(Vector, build.payload))