# src/space/stepper/quadrant/space.py

"""
Module: space.stepper.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from model import Vector
from register import NumberRegister
from result import ComputationResult
from space import Quadrant, Stepper
from util import LoggingLevelRouter


class QuadrantStepper(Stepper[Quadrant]):
    ENTRY = {
        "northeast": NumberRegister(a=1, b=-1),
        "northwest": NumberRegister(a=-1, b=-1),
        "southwest": NumberRegister(a=-1, b=1),
        "southeast": NumberRegister(a=1, b=1,)
    }
    _register: NumberRegister
    
    
    def __init__(self, x_step: int, slope: int,):
        """
        Args:
            x_step: int
            slope: int
        """
        super().__init__()
        self._register = NumberRegister(a=x_step, b=slope)
        
    @property
    def x_step(self) -> int:
        return self._register.a
    
    @property
    def slope(self) -> int:
        return self._register.b
    
    @LoggingLevelRouter.monitor
    def next(self, current: Vector) -> ComputationResult:
        method = f"{self.__class__.__name__}"
        
        build = self.math.vector.builder.execute(
            x=current.x,
            y=(2 * current.y * self.slope) + self.slope
        )
        
        if build.is_failure:
            return ComputationResult.failure(
                build.exception
            )
        return ComputationResult.success(cast(Vector, build.payload))
    
    
    @classmethod
    def northeast(cls) -> QuadrantStepper:
        return cls(
            x_step=cls.ENTRY["northeast"].a,
            slope=cls.ENTRY["northeast"].b,
        )
        
    @classmethod
    def northwest(cls) -> QuadrantStepper:
        return cls(
            x_step=cls.ENTRY["northwest"].a,
            slope=cls.ENTRY["northwest"].b,
        )
        
    @classmethod
    def southwest(cls) -> QuadrantStepper:
        return cls(
            x_step=cls.ENTRY["southwest"].a,
            slope=cls.ENTRY["southwest"].b,
        )
        
    @classmethod
    def southeast(cls) -> QuadrantStepper:
        return cls(
            x_step=cls.ENTRY["southeast"].a,
            slope=cls.ENTRY["southeast"].b,
        )