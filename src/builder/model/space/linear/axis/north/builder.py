# src/space/linear/axis/north/builder.py

"""
Module: space.linear.axis.north.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from builder import Builder, NorthAxisEndpointBuilder
from err import NorthAxisBuilderException
from math import NorthAxisStepper
from model import Vector
from register import VectorRegister
from result import BuildResult, MethodResultType
from space import NorthTraversalPattern
from util import LoggingLevelRouter
from validator import VectorValidator


class NorthAxisBuilder(Builder[NorthTraversalPattern]):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create an NorthAxis from the origin.

    Attributes:
        origin: Vector,
        stepper: Optional[AxisNorthAxisStepper]
        vector_validator: Optional[VectorValidator]

    Provides:
        -   def execute() -> BuildResult[NorthAxis]

    Super Class:
    """
    _origin: Vector
    _stepper: NorthAxisStepper
    _vector_validator: VectorValidator
    
    def __init__(
            self,
            origin: Vector,
            stepper: Optional[NorthAxisStepper] | None = NorthAxisStepper(),
            vector_validator: Optional[VectorValidator] | None = VectorValidator(),
    ):
        """
        Args:
            origin: Vector,
            stepper: Optional[AxisNorthAxisStepper]
            vector_validator: Optional[VectorValidator]
        """
        self._origin = origin
        self._stepper = stepper
        self._vector_validator = vector_validator
     
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[NorthTraversalPattern]:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the origin is flagged unsafe.
        validation = self._vector_validator.execute(canidate=self._origin)
        if validation.is_failure:
            # Handle the case that the request is not satisfied.
            if validation.is_failure:
                # Send the exception in the result.
                return BuildResult.failure(
                    NorthAxisBuilderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NorthAxisBuilderException.MSG,
                        err_code=NorthAxisBuilderException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.BUILD_RESULT,
                        ex=validation.exception
                    )
                )
        origin = cast(Vector, validation.payload)
        
        # Request a register of the endpoints.
        endpoint_request = NorthAxisEndpointBuilder(
            origin=self._origin,
        ).execute()
        # Handle the case that the request is not satisfied.
        if endpoint_request.is_failure:
            # Send the exception in the result.
            return BuildResult.failure(
                NorthAxisBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NorthAxisBuilderException.MSG,
                    err_code=NorthAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=endpoint_request.exception
                )
            )
        # Otherwise, extract and cast the product.
        endpoints = cast(VectorRegister, endpoint_request.payload)
        axis = NorthTraversalPattern(endpoints=endpoints, stepper=self._stepper)

        return BuildResult.success(axis)