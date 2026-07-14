# src/space/stepper/axis/space.py

"""
Module: space.stepper.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, cast

from model import Vector
from register import VectorRegister
from result import ComputationResult
from space import AxisSpace, Stepper
from util import LoggingLevelRouter


class AxisStepper(Stepper[AxisSpace]):
    DELTA = {
        "east": Vector(x=1, y=0),
        "north": Vector(x=0, y=-1),
        "south": Vector(x=0, y=1),
        "west": Vector(x=-1, y=0),
    }

    _delta: Vector
    
    def __init__(self, delta: Vector):
        super().__init__()
        self._delta = delta
        
    @property
    def delta(self) -> Vector:
        return self._delta
    
    @LoggingLevelRouter.monitor
    def next(self, u: Vector) -> ComputationResult[Vector]:
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
             AxisSpaceException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Safely add delta and current. ---#
        computation = self.math.add_vector.execute(
            VectorRegister(u=u, v=self._delta)
        )
        # Handle the case that, the computation is aborted.
        if computation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                computation.exception
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(cast(Vector, computation.payload))
    
    @classmethod
    def east(cls) -> AxisStepper:
        return cls(delta=cls.DELTA["east"])
    
    @classmethod
    def north(cls) -> AxisStepper:
        return cls(delta=cls.DELTA["north"])
    
    @classmethod
    def west(cls) -> AxisStepper:
        return cls(delta=cls.DELTA["west"])
    
    @classmethod
    def south(cls) -> AxisStepper:
        return cls(delta=cls.DELTA["south"])