# src/space/bounds/quadrant/space.py

"""
Module: space.bounds.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from model import Vector
from register import NumberRegister
from space import SpaceBounds
from space import QuadrantTerminusEntry


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