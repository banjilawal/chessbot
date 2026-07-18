# src/space/linear/section/linear.py

"""
Module: space.linear.section.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Vector
from register import VectorRegister


class LineSegment:
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Store upper and lower section of a Space. basic integrity and sanity checking.

    Attributes:
        origin: Vector
        terminus: Vector

    Provides:

    Super Class:
    """
    
    _endpoints: VectorRegister
    
    def __init__(self, origin: Vector, terminus: Vector):
        """
        Args:
            origin: Vector
            terminus: Vector
        """
        self._endpoints = VectorRegister(u=origin, v=terminus)
        
    @property
    def origin(self) -> Vector:
        return self._endpoints.u
    
    @property
    def terminus(self) -> Vector:
        return self._endpoints.v
    
    @property
    def is_empty(self) -> bool:
        return self._endpoints.is_empty
    
    @property
    def is_cycle(self) -> bool:
        return self._endpoints.u_is_v