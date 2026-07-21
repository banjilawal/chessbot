# src/space/linear/segment/axial/space.py

"""
Module: space.linear.segment.axial.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from builder.endpoint.axis.builder import AxisEndpointBuilder
from model import Vector
from register import VectorRegister
from result import BuildResult, ComputationResult
from schema import AxisTerminus
from space import WestTraversalPattern
from toolkit import MathToolkit
from util import LoggingLevelRouter
from validator import VectorValidator


class WestAxisEndpointBuilder(AxisEndpointBuilder[WestTraversalPattern]):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create a VectoRegister for an AxialSpace endpoints.

    Attributes:
        math_toolkit: Optional[MathToolkit]
        vector_validator: Optional[VectorValidator]

    Provides:
        -   def execute(origin: Vector) -> BuildResult[VectorRegister]

    Super Class:
    """
    _math_toolkit: MathToolkit
    _vector_validator: Optional[VectorValidator]
    
    def __init__(
            self,
            math_toolkit: Optional[MathToolkit] | None = MathToolkit(),
            vector_validator: Optional[VectorValidator] | None = VectorValidator(),
    ):
        """
        Args:
            math_toolkit: Optional[MathToolkit]
            vector_service: Optional[VectorValidator]
        """
        self._math_toolkit = math_toolkit
        self._vector_validator = vector_validator
        self._delta = Vector(
            x=origin.x + AxisTerminus.WEST.vector.x,
            y=0,
        )
        self._terminus =  Vector(
            x=AxisTerminus.WEST.vector.x,
            y=origin.y
        )

    @LoggingLevelRouter.monitor
    def execute(self, origin: Vector) -> ComputationResult[VectorRegister]:
        """
        Construct the endpoints for a WesternAxis instance.

        Action:
            1.  Send an exception chain in the BuildResult if the VectorValidator instance
                fails.
            2.  Otherwise, create the VectorRegister product and send in the success result.
        Args:
        Returns:
            BuildResult[VectorRegister]
        Raises:
             WesternAxisEndPointBuilderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the origin is not safe to use.
        validation = self._vector_validator.execute(origin)
        # Send the exception chain in the result.
        if validation.is_failure:
            return BuildResult.failure(
                WestAxisEndPointBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WestAxisEndPointBuilderException.MSG,
                    err_code=WestAxisEndPointBuilderException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        delta = Vector(
            x=origin.x + AxisTerminus.WEST.vector.x,
            y=0,
        )
        terminus_request = self._math_toolkit.vector.builder.execute(
            x=origin.x + delta.x,
            y=origin.y + delta.y,
        )
        if terminus_request.is_failure:
            return BuildResult.failure(
                WestAxisEndPointBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WestAxisEndPointBuilderException.MSG,
                    err_code=WestAxisEndPointBuilderException.ERR_CODE,
                    ex=terminus_request.exception,
                )
            )
        # Create the endpoint register.
        vector_register = VectorRegisterBuilder.execute(
            u=cast(Vector, validation.payload),
            v=self._terminus,
        )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(vector_register)
    #
    # @LoggingLevelRouter.monitor
    # def execute(self) -> BuildResult[VectorRegister]:
    #     """
    #     Construct the endpoints for a WesternAxis instance.
    #
    #     Action:
    #         1.  Send an exception chain in the BuildResult if the VectorValidator instance
    #             fails.
    #         2.  Otherwise, create the VectorRegister product and send in the success result.
    #     Args:
    #     Returns:
    #         BuildResult[VectorRegister]
    #     Raises:
    #          WesternAxisEndPointBuilderException
    #     """
    #     method = f"{self.__class__.__name__}.execute"
    #
    #     # Request a product from the vector builder.
    #     result = self._vector_service.execute(
    #         x=self._origin.x + self._delta.x,
    #         y=self._origin.y + self._delta.y,
    #     )
    #     # Handle the case that, the request is not fulfilled.
    #     if result.is_failure:
    #         return BuildResult.failure(
    #             WestAxisEndPointBuilderException(
    #                 cls_mthd=method,
    #                 cls_name=self.__class__.__name__,
    #                 msg=WestAxisEndPointBuilderException.MSG,
    #                 err_code=WestAxisEndPointBuilderException.ERR_CODE,
    #                 ex=result.exception,
    #             )
    #         )
        # Create the endpoint register.
        vector_register = VectorRegister(
            u=self._origin,
            v=cast(Vector, result.payload)
        )
        # --- Forward the work product to the caller. ---#
    #     return BuildResult.success(payload=vector_register)
