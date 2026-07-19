# src/space/linear/segment/quadrant/linear.py

"""
Module: space.linear.segment.quadrant.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from builder import LinearEndpointFactory
from model import Vector
from register import VectorRegister
from schema import QuadrantTerminus



class QuadrantEndpointFactory(LinearEndpointFactory):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create a VectoRegister for a QuadrantSpace endpoints.

    Attributes:
        origin: VectorRegister
        
    Provides:
        -   def northeast_endpoints() -> VectorRegister
        -   def northwest_endpoints() -> VectorRegister
        -   def southwest_endpoints() -> VectorRegister
        -   def southeast_endpoints() -> VectorRegister

    Super Class:
    """
    _origin: Vector
    
    def __init__(self, origin: Vector):
        """
        Args:
            origin: Vector
        """
        self._origin = origin
        
    @property
    def origin(self) -> Vector:
        return self._origin
        

    def northeast_endpoints(self) -> VectorRegister:
        return VectorRegister(
            u=self._origin,
            v=QuadrantTerminus.NORTHEAST.terminus,
        )
    
    def northwest_endpoints(self) -> VectorRegister:
        return VectorRegister(
            u=self._origin,
            v=QuadrantTerminus.NORTHWEST.terminus
        )
    
    def southeast_endpoints(self) -> VectorRegister:
        return VectorRegister(
            u=self._origin,
            v=QuadrantTerminus.SOUTHEAST.terminus
        )
    
    def southwest(self) -> VectorRegister:
        return VectorRegister(
            u=self._origin,
            v=QuadrantTerminus.SOUTHWEST.terminus
        )