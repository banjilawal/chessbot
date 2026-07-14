# src/space/stepper/quadrant/space.py

"""
Module: space.stepper.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from register import NumberRegister


class QuadrantStepper:
    _register: NumberRegister
    
    def __int__(self, x_step: int, slope: int,):
        self._register = NumberRegister(a=x_step, b=slope)
        
    @property
    def x_step(self) -> int:
        return self._register.a
    
    @property
    def slope(self) -> int:
        return self._register.b
    
    
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
        return cls.(x_step=1, slope=1,)
