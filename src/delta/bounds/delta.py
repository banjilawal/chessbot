# src/delta/bounds/delta.py

"""
Module: delta.bounds.delta
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from bounds import AxisBounds
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
