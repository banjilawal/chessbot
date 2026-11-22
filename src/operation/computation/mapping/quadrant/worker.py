# src/operation/computation/mapping/quadrant/worker.py

"""
Module: operation.computation.mapping.quadrant.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ComputationResult
from domain import Vector, VectorBlueprint
from operation import SpaceMappingFunction
from request import QuadrantMappingRequest, VectorBuildRequest

from transit import VectorCarrier

from util import IdFactory, LoggingLevelRouter



class QuadrantMappingFunction(SpaceMappingFunction[QuadrantMappingRequest]):
    """
    Role:
        - Computation

    Responsibilities:
        1.  Get the next vector, V, after U in Quadrant Space, using the linear functions:
                - V.x = U.x + x_step
                - V.y = (2 * slope * U.y) + slope

    Attributes:
        x_step: int
        slope: int

    Provides:
        def next(self, vector: Vector) -> ComputationResult[Vector]

    Super Class:
        SpaceMappingFunction
    """

    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, request: QuadrantMappingRequest) -> ComputationResult[Vector]:
        """
        Get the next Vector using a linear function.

        Action:
            1.  Set
                    x_next = x_current + x_step
                    y_next = (2 * slope * y_current) + slope
            2.  If VectorBuilder cannot create a safe Vector from x_next, y_next, send
                an exception chain in the ComputationResult.
            3.  Otherwise, cast the build product, then send in the success result.
        Args:
            request: QuadrantMappingRequest
        Returns:
            ComputationResult[Vector]
        Raises:
             QuadrantMappingFunctionException
        """
        method = f"{self.__class__.__name__}.next"
        
        # Handle the case that the argument is not safe to use.
        validation = self.math.vector.validator.execute(vector)
        if validation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                QuadrantMappingFunctionException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantMappingFunctionException.MSG,
                    err_code=QuadrantMappingFunctionException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=validation.exception,
                ),
            )
        vector = request.vector
        slope = request.slope
        x_step = request.x_step

        x = vector.x + x_step
        y = (2 * vector.y * slope) + slope
        
        result = self.vector_builder.execute(
            request=VectorBuildRequest(
                item=VectorCarrier(blueprint=VectorBlueprint(x=x, y=y)),
                id=IdFactory.next_id(class_name="Request")
            )
        )
        # Handle the case that the build is not successful.
        if result.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                QuadrantMappingFunctionException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantMappingFunctionException.MSG,
                    err_code=QuadrantMappingFunctionException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=result.exception,
                ),
            )
        value = cast(Vector, result.payload)
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(value)