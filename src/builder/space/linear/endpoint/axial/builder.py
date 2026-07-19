# src/space/linear/segment/axial/space.py

"""
Module: space.linear.segment.axial.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

import setting
from builder import LinearEndpointFactory, VectorBuilder

from model import Vector
from register import VectorRegister
from schema.terminus.axis import AxisTerminus



class AxisEndpointBuilder(LinearEndpointFactory):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create a VectoRegister for an AxialSpace endpoints.

    Attributes:
        _origin: Vector
        _vector_builder: VectorBuilder

    Provides:
        -   def eastern_endpoints() -> VectorRegister
        -   def northern_endpoints() -> VectorRegister
        -   def western_endpoints() -> VectorRegister
        -   def southern_endpoints() -> VectorRegister

    Super Class:
    """
    _origin: Vector
    _vector_builder: VectorBuilder
    
    def __init__(
            self,
            origin: Vector,
            vector_builder: Optional[VectorBuilder] | None = VectorBuilder()
    ):
        """
        Args:
            origin: Vector
            vector_builder: Optional[VectorBuilder]
        """
        self._origin = origin
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def vector_builder(self) -> VectorBuilder:
        return self._vector_builder
    
    def eastern_endpoints(self) -> VectorRegister:
        """
        East towards num_columns - 1 (right)
        """
        return VectorRegister(
            u=self._origin,
            v = Vector(
                x=self._origin.x + AxisTerminus.EAST.delta.x,
                y=self._origin.y+ AxisTerminus.EAST.delta.y,
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
        return VectorRegist er(
            u=self._origin,
            v=Vector(
                x=self._origin.x + AxisTerminus.SOUTH.delta.x,
                y=self._origin.y + AxisTerminus.SOUTH.delta.y,
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