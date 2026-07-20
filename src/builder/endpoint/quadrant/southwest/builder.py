# src/builder/endpoint/quadrant/southwest/builder.py

"""
Module: builder.endpoint.quadrant.southwest.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional


from model import Vector
from register import VectorRegister
from result import BuildResult
from schema.terminus.quadrant import QuadrantTerminus
from util import LoggingLevelRouter
from validator import VectorValidator


class SouthwestQuadrantEndpointBuilder:
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create a VectorRegister for the quadrant southwest of the origin.

    Attributes:
        origin: Vector
        terminus: Vector
        vector_validator: Optional[VectorValidator]
        
    Provides:
        -   def execute() -> BuildResult[VectorRegister]

    Super Class:
    """
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
        self._terminus = QuadrantTerminus.SOUTHWEST.vector
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
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
                SouthwestQuadrantEndPointBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SouthwestQuadrantEndPointBuilderException.MSG,
                    err_code=SouthwestQuadrantEndPointBuilderException.ERR_CODE,
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
    