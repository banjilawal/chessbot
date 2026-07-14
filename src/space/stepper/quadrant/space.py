# src/space/stepper/quadrant/space.py

"""
Module: space.stepper.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Vector
from register import NumberRegister
from result import ComputationResult
from space import Quadrant, Stepper
from util import LoggingLevelRouter


class QuadrantStepper(Stepper):
    _register: NumberRegister
    
    def __int__(self, x_step: int, slope: int,):
        """
        Args:
            x_step: int
            slope: int
        """
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
        return cls(x_step=1, slope=-1,)
        
    @classmethod
    def northwest(cls) -> QuadrantStepper:
        return cls(x_step=-1, slope=-1,)
        
    @classmethod
    def southwest(cls) -> QuadrantStepper:
        return cls(x_step=-1, slope=1,)
        
    @classmethod
    def southeast(cls) -> QuadrantStepper:
        return cls(x_step=1, slope=1,)