# src/space/axis/terminus/bounds/space/axis/space.axis.terminus.py

"""
Module: space.axis.terminus.bounds.terminus
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from space.bounds import AxisBounds
from model import Vector
from register import Register


class terminusBound(Register):
    
    def __init__(self, terminus: Vector, bounds: AxisBounds):
        super().__init__(a=terminus, b=bounds)
        
    @property
    def terminus(self) -> Vector:
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
