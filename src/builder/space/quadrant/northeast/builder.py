# src/builder/space/quadrant/northeast/__init__.py

"""
Module: builder.space.quadrant.northeast.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from builder import QuadrantSpaceBuilder
from err import NortheastQuadrantBuilderException
from model import Vector, vector
from result import BuildResult, MethodResultType
from space import NortheastQuadrant


class NorthEastQuadrantBuilder(QuadrantSpaceBuilder[NortheastQuadrant]):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:

    Provides:
        -   def execute(origin: Vector) -> BuildResult[EastAxis]

    Super Class:
    """
    super().__init__()
    

    _origin: Vector
    _stepper: NortheastQuadrantStepper
    _vector_validator: VectorValidator
    
    def __init__(
            self,
            origin: Vector,
            stepper: Optional[NortheastQuadrantStepper] | None = NortheastQuadrantStepper(),
            vector_validator: Optional[VectorValidator] | None = VectorValidator(),
    ):
        """
        Args:
            origin: Vector,
            stepper: Optional[NortheastQuadrantStepper]
            vector_validator: Optional[VectorValidator]
        """
        self._origin = origin
        self._stepper = stepper
        self._vector_validator = vector_validator
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[NortheastTraversalPattern]:

        
        # Request a register of the endpoints.
        endpoint_request = NortheastQuadrantEndpointBuilder(
            origin=origin,
        ).execute()
        # Handle the case that the request is not satisfied.
        if endpoint_request.is_failure:
            # Send the exception in the result.
            return BuildResult.failure(
                NortheastQuadrantBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NortheastQuadrantBuilderException.MSG,
                    err_code=NortheastQuadrantBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=endpoint_request.exception
                )
            )
        # Otherwise, extract and cast the product.
        endpoints = cast(VectorRegister, endpoint_request.payload)
        quadrant = NortheastTraversalPattern(endpoints=endpoints, stepper=self._stepper)
        
        return BuildResult.success(quadrant)
    
    def execute(self, origin: Vector) -> BuildResult[NortheastQuadrant]:
        method = f"{self.__class__.__name__}.execute"
        
        validation = self.math.vector.validator.execult(origin)
        if validation.is_failure:
            # Handle the case that the request is not satisfied.
            if validation.is_failure:
                # Send the exception in the result.
                return BuildResult.failure(
                    NortheastQuadrantBuilderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NortheastQuadrantBuilderException.MSG,
                        err_code=NortheastQuadrantBuilderException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.BUILD_RESULT,
                        ex=validation.exception
                    )
                )
        return BuildResult.success(NortheastQuadrant(vector))