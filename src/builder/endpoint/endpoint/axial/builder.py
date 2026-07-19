# src/space/linear/segment/axial/space.py

"""
Module: space.linear.segment.axial.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


import setting


from model import Vector
from register import VectorRegister



class AxisEndpointFactory(LinearEndpointFactory):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create a VectoRegister for an AxialSpace endpoints.

    Attributes:
        _origin: Vector

    Provides:
        -   def eastern_endpoints() -> VectorRegister
        -   def northern_endpoints() -> VectorRegister
        -   def western_endpoints() -> VectorRegister
        -   def southern_endpoints() -> VectorRegister

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
    
    
    def eastern_endpoints(self) -> VectorRegister:
        """
        East towards num_columns - 1 (right)
        """
        return VectorRegister(
            u=self._origin,
            v = Vector(
                x=setting.board.dimension.config.number_of_columns - 1,
                y=self._origin.y,
            )
        )
    

    def northern_endpoints(self) -> VectorRegister:
        """
        North towards 0  (up)
        """
        return VectorRegister(
            u=self._origin,
            v=Vector(x=self._origin.x, y=0),
        )
    
    def southern_endpoints(self) -> VectorRegister:
        """
        South towards num_rows - 1 (up)
        """
        return VectorRegister(
            u=self._origin,
            v=Vector(
                x=self._origin.x,
                y=setting.board.dimension.config.number_of_rows - 1,
            )
        )
    
    def western_endpoints(self) -> VectorRegister:
        """
        West towards 0 (left)
        """
        return VectorRegister(
            u=self._origin,
            v=Vector(x=0, y=self._origin.y)
        )