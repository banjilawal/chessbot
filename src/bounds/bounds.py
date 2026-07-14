# src/bounds/bounds.py

"""
Module: bounds.bounds
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from model import Vector
from register import Register


class RayBounds(Register[]):
    endpoints: Register[Vector]
    
    def bounds(self, origin: Vector, terminus: Vector):
        endpoints =
        
    @property
    def origin(self) -> Vector:
        return cast(Vector, self.a)
    
    @property
    def