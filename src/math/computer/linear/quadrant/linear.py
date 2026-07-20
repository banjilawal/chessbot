# src/math/stepper/quadrant/math.py

"""
Module: math.stepper.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from err import QuadrantStepperException
from model import Vector
from result import ComputationResult, MethodResultType
from space import LinearStepper
from util import LoggingLevelRouter


class QuadrantStepper(LinearStepper):
    """
    Role:
        -   Computation Worker
        
    Background:
    1.  Consider the diagonal series: p_1(0,0), p_2(1,1), p_3(2,2), ., p_n(n,n). For any
            p_i, y_i = x_i.
        We want to find some invariant only in terms of x that will gives us all the ys.
    2.  Let us consider x in non-negative integers, {0, 1, 2,3,.,n}
        we now that
            x_i <= x_j < x_n.
    3.  The start of the X sequence is
            X_0 = 0,
            X_1 = 1,
            x_2 = 2
            x_3 = 3
       Which reveals: x_j = x_i + (j-i) But we want to express only in terms of x and restrict that i < j
            when i = 0, xo = x
            x_i = x_(i-1) + 1
    5. Since x_i = y_i, we can express the series in terms of x_(i-i)
            y_i = (x_(i-1) + delta_x) + x_(i-1)
            y_i = 2x_(i-1)
    6. In the quadrant(x<0, y>0) delta_x = -1.
    7. For thr quadrant (x<0, y>0) delta_x = 1.
    8. So for each quadrant we change the slope.
    
    Gives us
        abs(x_step) = 1,
        f = x + c where c is the step.
        g = 2bx + b where b is the slope.
        so
        v = ((u.x + c), ((2b)u.x + b)

    Responsibilities:
        1.  Produce y from the  range of x in a seres projected from the quadrant's origin.

    Attributes:
        x_step: int
        slope: int

    Provides:
        -   def next(current: Vector) -> ComputationResult[Vector]

    Super Class:
        Stepper
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
    def next(self, current: Vector) -> ComputationResult[Vector]:
        """
        Project a new, safe, vector, from the current.

        Action:
            1.  Set
                    x_next = x_current + x_step
                    y_next = (2 * slope * y_current) + slope
            2.  If VectorBuilder cannot create a safe Vector from x_next, y_next, send
                an exception chain in the ComputationResult.
            3.  Otherwise, cast the build product, then send in the success result.
        Args:
            current: Vector
        Returns:
            ComputationResult[Vector]
        Raises:
             QuadrantStepperException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Build a new vector from the old. ---#
        build = self.math.vector.builder.execute(
            x=current.x + self.x_step,
            y=(2 * current.y * self.slope) + self.slope
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