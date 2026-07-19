# src/space/linear/segment/axial/space.py

"""
Module: space.linear.segment.axial.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from builder import VectorBuilder
from err import NorthAxisEndPointBuilderException
from model import Vector
from register import VectorRegister
from result import BuildResult
from schema.terminus.axis import AxisTerminus
from util import LoggingLevelRouter


class NorthernAxisEndpointBuilder:
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create a VectoRegister for an AxialSpace endpoints.

    Attributes:
        delta: Vector

    Provides:
        -   def execute() -> BuildResult[VectorRegister]

    Super Class:
    """
    _delta: Vector
    _origin: Vector
    _vector_builder: VectorBuilder
    
    def __init__(
            self,
            origin: Vector,
            vector_builder: Optional[VectorBuilder] | None = VectorBuilder(),
    ):
        """
        Args:
            origin: Vector
            vector_builder: Optional[VectorBuilder]
        """
        self._origin = origin
        self._vector_builder = vector_builder
        self._delta = Vector(
            x=origin.x + AxisTerminus.NORTH.delta.x,
            y=origin.y + AxisTerminus.NORTH.delta.y,
        )
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def delta(self) -> Vector:
        return self._delta
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[VectorRegister]:
        """
        Construct the endpoints for a NorthernAxis instance.

        Action:
            1.  Send an exception chain in the BuildResult if the VectorBuilder instance
                fails.
            2.  Otherwise, create the VectorRegister product and send in the success result.
        Args:
        Returns:
            BuildResult[VectorRegister]
        Raises:
             NorthernAxisEndPointBuilderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Request a product from the vector builder.
        result = self._vector_builder.execute(
            x=self._origin.x + self._delta.x,
            y=self._origin.y + self._delta.y,
        )
        # Handle the case that, the request is not fulfilled.
        if result.is_failure:
            return BuildResult.failure(
                NorthAxisEndPointBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NorthAxisEndPointBuilderException.MSG,
                    err_code=NorthAxisEndPointBuilderException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # Create the endpoint register.
        vector_register = VectorRegister(
            u=self._origin,
            v=cast(Vector, result.payload)
        )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(payload=vector_register)
