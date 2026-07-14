# src/space/axis/delta/bounds/space/axis/space.axis.delta.py

"""
Module: space.axis.delta.bounds.delta
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from ray.bounds import AxisBounds
from model import Vector
from register import Register


class DeltaBound(Register):
    
    def __init__(self, delta: Vector, bounds: AxisBounds):
        super().__init__(a=delta, b=bounds)
        
    @property
    def delta(self) -> Vector:
        return cast(Vector, self.a)
    
    @property
    def bounds(self) -> AxisBounds:
        return cast(AxisBounds, self.b)
    
    @property
    def origin(self) -> Vector:
        return self.bounds.origin
    
    @property
    def terminus(self) -> Vector:
        return self.bounds.terminus
