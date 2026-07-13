# src/ray/register/axis/register.py

"""
Module: ray.register.axis.register
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Vector
from register import Axis


class AxisRayRegister:
    _axis: Axis
    _terminus: Vector
    
    def __init__(self, axis: Axis, terminus: Vector):
        self._axis = axis
        self._terminus = terminus
        
    @property
    def axis(self) -> Axis:
        return self.axis
    
    @property
    def terminus(self) -> Vector:
        return self._terminus
    
    
    
    