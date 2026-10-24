# src/space/linear/segment/axis/space.py

"""
Module: space.linear.segment.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from transit.dispatcher.attack.endpoint.axis.attack import AxisEndpointAttack
from domain.model import Vector
from domain.struct.register import VectorRegister
from artifcat import AttackResult, ComputationResult
from domain.schema import AxisDestination
from surface.space import WestTraversalPattern
from operation.toolkit import MathToolkit
from util import LoggingLevelRouter
from transit.dispatcher.validator import VectorValidator


class WestAxisEndpointAttack(AxisEndpointAttack[WestTraversalPattern]):
    """
    Role:
        - Attack
        - Integrity Management

    Responsibilities:
        1.  Create a VectoRegister for an Axis endpoints.

    Attributes:
        math_toolkit: Optional[MathToolkit]
        vector_validator: Optional[VectorValidator]

    Provides:
        -   def execute(origin: Vector) -> AttackResult[VectorRegister]

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
            x=origin.x + AxisDestination.WEST.vector.x,
            y=0,
        )
        self._destination =  Vector(
            x=AxisDestination.WEST.vector.x,
            y=origin.y
        )

    @LoggingLevelRouter.monitor
    def execute(self, origin: Vector) -> ComputationResult[VectorRegister]:
        """
        Construct the endpoints for a WesternAxis instance.

        Action:
            1.  Send an exception chain in the AttackResult if the VectorValidator instance
                fails.
            2.  Otherwise, create the VectorRegister product and send in the success result.
        Args:
        Returns:
            AttackResult[VectorRegister]
        Raises:
             WesternAxisEndPointAttackException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the origin is not safe to use.
        validation = self._vector_validator.execute(origin)
        # Send the exception chain in the result.
        if validation.is_failure:
            return AttackResult.failure(
                WestAxisEndPointAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WestAxisEndPointAttackException.MSG,
                    err_code=WestAxisEndPointAttackException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        delta = Vector(
            x=origin.x + AxisDestination.WEST.vector.x,
            y=0,
        )
        destination_request = self._math_toolkit.vector.attack.execute(
            x=origin.x + delta.x,
            y=origin.y + delta.y,
        )
        if destination_request.is_failure:
            return AttackResult.failure(
                WestAxisEndPointAttackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WestAxisEndPointAttackException.MSG,
                    err_code=WestAxisEndPointAttackException.ERR_CODE,
                    ex=destination_request.exception,
                )
            )
        # Create the endpoint register.
        vector_register = VectorRegisterAttack.execute(
            u=cast(Vector, validation.payload),
            v=self._destination,
        )
        # --- Forward the work product to the caller. ---#
        return AttackResult.success(vector_register)
    #
    # @LoggingLevelRouter.monitor
    # def execute(self) -> AttackResult[VectorRegister]:
    #     """
    #     Construct the endpoints for a WesternAxis instance.
    #
    #     Action:
    #         1.  Send an exception chain in the AttackResult if the VectorValidator instance
    #             fails.
    #         2.  Otherwise, create the VectorRegister product and send in the success result.
    #     Args:
    #     Returns:
    #         AttackResult[VectorRegister]
    #     Raises:
    #          WesternAxisEndPointAttackException
    #     """
    #     method = f"{self.__class__.__name__}.execute"
    #
    #     # Request a product from the vector attack.
    #     result = self._vector_service.execute(
    #         x=self._origin.x + self._delta.x,
    #         y=self._origin.y + self._delta.y,
    #     )
    #     # Handle the case that the request is not fulfilled.
    #     if result.is_failure:
    #         return AttackResult.failure(
    #             WestAxisEndPointAttackException(
    #                 cls_mthd=method,
    #                 cls_name=self.__class__.__name__,
    #                 msg=WestAxisEndPointAttackException.MSG,
    #                 err_code=WestAxisEndPointAttackException.ERR_CODE,
    #                 ex=result.exception,
    #             )
    #         )
        # Create the endpoint register.
        vector_register = VectorRegister(
            u=self._origin,
            v=cast(Vector, result.payload)
        )
        # --- Forward the work product to the caller. ---#
    #     return AttackResult.success(payload=vector_register)
