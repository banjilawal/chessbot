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
from space import Axis, Stepper
from util import LoggingLevelRouter


class AxisDeltaEntry(Stepper[Axis]):
    
    _entry: Dict[str, Vector]
    
    def __init__(self):
        self._entry = {
            "east": Vector(x=1, y=0),
            "north": Vector(x=0, y=-1),
            "south": Vector(x=0, y=1),
            "west": Vector(x=-1, y=0),
        }
        
    @property
    def east(self) -> Vector:
        return self._entry["east"]
    
    @property
    def north(self) -> Vector:
        return self._entry["north"]
    
    @property
    def west(self) -> Vector:
        return self._entry["west"]
    
    @property
    def south(self) -> Vector:
        return self._entry["south"]
    
    @LoggingLevelRouter.monitor
    def next(self, u: Vector, space: Axis) -> ComputationResult:
        method = f"{self.__class__.__name__}"
        
        computation = self.math.add_vector.execute(
            VectorRegister(u=u, v=space.delta)
        )
        if computation.is_failure:
            return ComputationResult.failure(
                computation.exception
            )
        return computation