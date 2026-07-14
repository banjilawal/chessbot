# src/space/stepper/axis/space.py

"""
Module: space.stepper.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

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
    def next(self, u: Vector) -> ComputationResult:
        method = f"{self.__class__.__name__}"
        
        computation = self.math.add_vector.execute(
            VectorRegister(u=u, v=self._delta)
        )
        if computation.is_failure:
            return ComputationResult.failure(
                computation.exception
            )
        return computation
    
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