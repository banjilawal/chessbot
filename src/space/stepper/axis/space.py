# src/space/stepper/axis/space.py

"""
Module: space.stepper.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, cast

from err import AxisSpaceSetterException
from model import Vector
from register import VectorRegister
from result import ComputationResult, MethodResultType
from space import AxisSpace, Stepper
from util import LoggingLevelRouter


class AxisStepper(Stepper[AxisSpace]):
    """
    Role:
        -   Lookup Table

    Responsibilities:
        1.  Produce the next vector on axis by taking a step of size delta_vector.

    Attributes:
        DELTA: Dict[str, Vector]
        delta: Vector

    Provides:
        -   next(current: Vector) -> ComputationResult[Vector]
        -   east() -> AxisStepper
        -   north() -> AxisStepper
        -   west() -> AxisStepper
        -   south() -> AxisStepper

    Super Class:
        Stepper
    
    WARNING:
        *****===ONLY_INSTANTIATE_WITH_THE_FACTORY_METHODS===*****
    """
    DELTA: Dict[str, Vector] = {
        "east": Vector(x=1, y=0),
        "north": Vector(x=0, y=-1),
        "south": Vector(x=0, y=1),
        "west": Vector(x=-1, y=0),
    }

    _delta: Vector
    
    def __init__(self, delta: Vector):
        """
        Args:
            delta: Vector
        """
        super().__init__()
        """INTERNAL: Use factory methods instead of direct constructor."""
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
                AxisSpaceSetterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisSpaceSetterException.MSG,
                    err_code=AxisSpaceSetterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=computation.exception,
                ),
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(cast(Vector, computation.payload))
    
    @classmethod
    def east(cls) -> AxisStepper:
        """
        AxisStepper for going east (right), towards num_columns - 1.
            -   delta ==> dx(1, 0)
        """
        return cls(delta=cls.DELTA["east"])
    
    @classmethod
    def north(cls) -> AxisStepper:
        """
        AxisStepper for going north (up), towards 0
            -   delta ==> dy(0, -1)
        """
        return cls(delta=cls.DELTA["north"])
    
    @classmethod
    def west(cls) -> AxisStepper:
        """
        AxisStepper for going west (left), towards 0
            -   delta ==> dx(-1, 0)
        """
        return cls(delta=cls.DELTA["west"])
    
    @classmethod
    def south(cls) -> AxisStepper:
        """
        AxisStepper for going south (down), towards 0
            -   delta ==> dy(0, 1)
        """
        return cls(delta=cls.DELTA["south"])