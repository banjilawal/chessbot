# src/space/linear/quadrant/southwest/builder.py

"""
Module: space.linear.quadrant.southwest.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from builder import Builder, SouthwestQuadrantEndpointBuilder
from err import SouthwestQuadrantBuilderException
from math import SouthwestQuadrantStepper
from model import Vector
from register import VectorRegister
from result import BuildResult, MethodResultType
from space import SouthwestQuadrant
from util import LoggingLevelRouter
from validator import VectorValidator


class SouthwestQuadrantBuilder(Builder[SouthwestQuadrant]):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
        origin: Vector,
        stepper: Optional[SouthwestQuadrantStepper]
        vector_validator: Optional[VectorValidator]

    Provides:
        -   def execute() -> BuildResult[EastAxis]

    Super Class:
    """
    _origin: Vector
    _stepper: SouthwestQuadrantStepper
    _vector_validator: VectorValidator
    
    def __init__(
            self,
            origin: Vector,
            stepper: Optional[SouthwestQuadrantStepper] | None = SouthwestQuadrantStepper(),
            vector_validator: Optional[VectorValidator] | None = VectorValidator(),
    ):
        """
        Args:
            origin: Vector,
            stepper: Optional[SouthwestQuadrantStepper]
            vector_validator: Optional[VectorValidator]
        """
        self._origin = origin
        self._stepper = stepper
        self._vector_validator = vector_validator
     
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[SouthwestQuadrant]:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the origin is flagged unsafe.
        validation = self._vector_validator.execute(canidate=self._origin)
        if validation.is_failure:
            # Handle the case that the request is not satisfied.
            if validation.is_failure:
                # Send the exception in the result.
                return BuildResult.failure(
                    SouthwestQuadrantBuilderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SouthwestQuadrantBuilderException.MSG,
                        err_code=SouthwestQuadrantBuilderException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.BUILD_RESULT,
                        ex=validation.exception
                    )
                )
        origin = cast(Vector, validation.payload)
        
        # Request a register of the endpoints.
        endpoint_request = SouthwestQuadrantEndpointBuilder(
            origin=self._origin,
        ).execute()
        # Handle the case that the request is not satisfied.
        if endpoint_request.is_failure:
            # Send the exception in the result.
            return BuildResult.failure(
                SouthwestQuadrantBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SouthwestQuadrantBuilderException.MSG,
                    err_code=SouthwestQuadrantBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=endpoint_request.exception
                )
            )
        # Otherwise, extract and cast the product.
        endpoints = cast(VectorRegister, endpoint_request.payload)
        quadrant = SouthwestQuadrant(endpoints=endpoints, stepper=self._stepper)

        return BuildResult.success(quadrant)