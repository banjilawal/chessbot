# src/space/space.py

"""
Module: space.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import cast

from model import Vector

class Space(ABC):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Define a 2D space bounded an origin and terminus.

    Attributes:
        origin: Vector
        terminus: Vector


    Provides:

    Super Class:
    """
    _origin: Vector
    _terminus: Vector
    
    
    def __init__(self, origin: Vector, terminus: Vector):
        self._origin = origin
        self._terminus = terminus
        
    
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def terminus(self) -> Vector:
        return self._terminus
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Space):
            space = cast(Space, other)
            return self._origin == space.origin and self._terminus == space.terminus
        return False