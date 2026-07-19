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
from err import SouthwestQuadrantEndPointBuilderException
from model import Vector
from register import VectorRegister
from result import BuildResult
from schema.terminus.quadrant import QuadrantTerminus
from util import LoggingLevelRouter


class SouthwestQuadrantEndpointBuilder:
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create a VectoRegister for an AxialSpace endpoints.

    Attributes:
        delta: Vector
        origin: Vector
        vector_builder: Optional[VectorBuilder]

    Provides:
        -   def execute() -> BuildResult[VectorRegister]

    Super Class:
    """
    _delta: Vector
    _origin: Vector
    _terminus: Vector
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
            x=origin.x + QuadrantTerminus.SOUTHWEST.vector.x,
            y=0,
        )
        self._terminus =  Vector(
            x=QuadrantTerminus.SOUTHWEST.vector.x,
            y=origin.y
        )
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def delta(self) -> Vector:
        return self._delta
    
    @property
    def terminus(self) -> Vector:
        return self._terminus
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[VectorRegister]:
        return BuildResult.success(
            VectorRegister(u=self._origin, v=self._terminus)
        )
    #
    # @LoggingLevelRouter.monitor
    # def execute(self) -> BuildResult[VectorRegister]:
    #     """
    #     Construct the endpoints for a SouthwesternQuadrant instance.
    #
    #     Action:
    #         1.  Send an exception chain in the BuildResult if the VectorBuilder instance
    #             fails.
    #         2.  Otherwise, create the VectorRegister product and send in the success result.
    #     Args:
    #     Returns:
    #         BuildResult[VectorRegister]
    #     Raises:
    #          SouthwesternQuadrantEndPointBuilderException
    #     """
    #     method = f"{self.__class__.__name__}.execute"
    #
    #     # Request a product from the vector builder.
    #     result = self._vector_builder.execute(
    #         x=self._origin.x + self._delta.x,
    #         y=self._origin.y + self._delta.y,
    #     )
    #     # Handle the case that, the request is not fulfilled.
    #     if result.is_failure:
    #         return BuildResult.failure(
    #             SouthwestQuadrantEndPointBuilderException(
    #                 cls_mthd=method,
    #                 cls_name=self.__class__.__name__,
    #                 msg=SouthwestQuadrantEndPointBuilderException.MSG,
    #                 err_code=SouthwestQuadrantEndPointBuilderException.ERR_CODE,
    #                 ex=result.exception,
    #             )
    #         )
    #     # Create the endpoint register.
    #     vector_register = VectorRegister(
    #         u=self._origin,
    #         v=cast(Vector, result.payload)
    #     )
    #     # --- Forward the work product to the caller. ---#
    #     return BuildResult.success(payload=vector_register)
