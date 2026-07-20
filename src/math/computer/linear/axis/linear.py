# src/math/stepper/axis/linear.py

"""
Module: math.stepper.axis.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from err import AxisStepperException
from math import LinearTargetVectorComputer
from model import Vector
from register import VectorRegister
from result import ComputationResult, MethodResultType
from util import LoggingLevelRouter


class AxisStepper(LinearTargetVectorComputer):
    """
    Role:
        -   Computation Worker

    Responsibilities:
        1.  Produce the next vector on axis by taking a step of size delta_vector.

    Attributes:
        delta: Vector

    Provides:
        -   next(current: Vector) -> ComputationResult[Vector]

    Super Class:
        Stepper
    """
    _delta: Vector
    
    def __init__(self, delta: Vector):
        """
        Args:
            delta: Vector
        """
        super().__init__()
        self._delta = delta
        
    @property
    def delta(self) -> Vector:
        return self._delta
    
    @LoggingLevelRouter.monitor
    def next(self, current: Vector) -> ComputationResult[Vector]:
        """
        Project a new, safe, vector, from the current.

        Action:
            1.  If VectorAdder cannot produce a solution, send an exception chain in the reesult.
            2.  Otherwise, send the cast product in the success result.
        Args:
            current: Vector
        Returns:
            ComputationResult[Vector]
        Raises:
             AxisStepperException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Safely add delta and current. ---#
        computation = self.math.add_vector.execute(
            VectorRegister(u=current, v=self._delta)
        )
        # Handle the case that, the computation is aborted.
        if computation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                AxisStepperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisStepperException.MSG,
                    err_code=AxisStepperException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=computation.exception,
                ),
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(cast(Vector, computation.payload))
 