# src/space/linear/segment/axial/space.py

"""
Module: space.linear.segment.axial.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from builder import VectorValidator
from err import SouthAxisEndPointBuilderException
from model import Vector
from register import VectorRegister
from result import BuildResult
from schema.terminus.axis import AxisTerminus
from util import LoggingLevelRouter


class SouthAxisEndpointBuilder:
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create a VectoRegister for an AxialSpace endpoints.

    Attributes:
        delta: Vector
        origin: Vector
        vector_validator: Optional[VectorValidator]

    Provides:
        -   def execute() -> BuildResult[VectorRegister]

    Super Class:
    """
    _delta: Vector
    _origin: Vector
    _terminus: Vector
    _vector_validator: VectorValidator
    
    def __init__(
            self,
            origin: Vector,
            vector_validator: Optional[VectorValidator] | None = VectorValidator(),
    ):
        """
        Args:
            origin: Vector
            vector_validator: Optional[VectorValidator]
        """
        self._origin = origin
        self._vector_validator = vector_validator
        self._delta = Vector(
            x=origin.x + AxisTerminus.SOUTH.vector.x,
            y=origin.y + AxisTerminus.SOUTH.vector.y,
        )
        self._terminus = Vector(
            x=self._origin.x,
            y=AxisTerminus.SOUTH.vector.y
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
        """
        Construct the endpoints for a SouthernAxis instance.

        Action:
            1.  Send an exception chain in the BuildResult if the VectorValidator instance
                fails.
            2.  Otherwise, create the VectorRegister product and send in the success result.
        Args:
        Returns:
            BuildResult[VectorRegister]
        Raises:
             SouthernAxisEndPointBuilderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the origin is not safe to use.
        validation = self._vector_validator.execute(self._origin)
        # Send the exception chain in the result.
        if validation.is_failure:
            return BuildResult.failure(
                SouthAxisEndPointBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SouthAxisEndPointBuilderException.MSG,
                    err_code=SouthAxisEndPointBuilderException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # Create the endpoint register.
        vector_register = VectorRegister(
            u=cast(Vector, validation.payload),
            v=self._terminus,
        )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(vector_register)
    
    # @LoggingLevelRouter.monitor
    # def execute(self) -> BuildResult[VectorRegister]:
    #     """
    #     Construct the endpoints for a SouthernAxis instance.
    #
    #     Action:
    #         1.  Send an exception chain in the BuildResult if the VectorValidator instance
    #             fails.
    #         2.  Otherwise, create the VectorRegister product and send in the success result.
    #     Args:
    #     Returns:
    #         BuildResult[VectorRegister]
    #     Raises:
    #          SouthernAxisEndPointBuilderException
    #     """
    #     method = f"{self.__class__.__name__}.execute"
    #
    #     # Request a product from the vector builder.
    #     result = self._vector_validator.execute(
    #         x=self._origin.x + self._delta.x,
    #         y=self._origin.y + self._delta.y,
    #     )
    #     # Handle the case that, the request is not fulfilled.
    #     if result.is_failure:
    #         return BuildResult.failure(
    #             SouthAxisEndPointBuilderException(
    #                 cls_mthd=method,
    #                 cls_name=self.__class__.__name__,
    #                 msg=SouthAxisEndPointBuilderException.MSG,
    #                 err_code=SouthAxisEndPointBuilderException.ERR_CODE,
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
