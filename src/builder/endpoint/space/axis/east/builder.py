# src/space/linear/segment/axial/space.py

"""
Module: space.linear.segment.axial.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Vector
from register import VectorRegister
from result import BuildResult
from schema.terminus.axis import AxisTerminus
from util import LoggingLevelRouter


class EastAxisEndpointBuilder:
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create a VectoRegister for an AxialSpace endpoints.

    Attributes:
        origin: Vector
        
    Provides:
        -   def execute() -> BuildResult[VectorRegister]

    Super Class:
    """
    _origin: Vector
    _terminus: Vector
    
    def __init__(self, origin: Vector,):
        """
        Args:
            origin: Vector
        """
        self._origin = origin
        self._terminus = AxisTerminus.EAST.vector
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def terminus(self) -> Vector:
        return self._terminus
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[VectorRegister]:
        return BuildResult.success(
            VectorRegister(u=self._origin, v=self._terminus)
        )
    
    # @LoggingLevelRouter.monitor
    # def execute(self) -> BuildResult[VectorRegister]:
    #     """
    #     Construct the endpoints for a EastAxis instance.
    #
    #     Action:
    #         1.  Send an exception chain in the BuildResult if the VectorBuilder instance
    #             fails.
    #         2.  Otherwise, create the VectorRegister product and send in the success result.
    #     Args:
    #     Returns:
    #         BuildResult[VectorRegister]
    #     Raises:
    #          EastAxisEndPointBuilderException
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
    #             EastAxisEndPointBuilderException(
    #                 cls_mthd=method,
    #                 cls_name=self.__class__.__name__,
    #                 msg=EastAxisEndPointBuilderException.MSG,
    #                 err_code=EastAxisEndPointBuilderException.ERR_CODE,
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
