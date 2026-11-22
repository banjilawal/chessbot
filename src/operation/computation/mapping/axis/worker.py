# src/operation/computation/mapping/axis/worker.py

"""
Module: operation.computation.mapping.axis.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import Vector, VectorNode
from err import AxisNodeStepFunctionException, VectorNullException

from artifcat import ComputationResult, MethodResultType
from operation import SpaceNodeStepFunction
from request import AxisMappingRequest, VectorAdditionRequest
from util import IdFactory, LoggingLevelRouter



class AxisNodeStepFunction(SpaceNodeStepFunction[AxisMappingRequest]):
    """
    Role:
        - Computation

    Responsibilities:
        1.  Get the next vector, V, after U in Axis Space, by addition of a delta_vector
                - V.x = U.x + delta.x
                - V.y = U.x + delta.y

    Attributes:

    Provides:
        def execute(request: AxisMappingRequest) -> ComputationResult[Vector]

    Super Class:
        SpaceNodeStepFunction
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()

    
    @LoggingLevelRouter.monitor
    def execute(self, request: AxisMappingRequest) -> ComputationResult[VectorNode]:
        """
        Get the next Vector using addition.

        Action:
            1.  Set
                    x_next = x_current + x_step
                    y_next = (2 * slope * y_current) + slope
            2.  If VectorBuilder cannot create a safe Vector from x_next, y_next, send
                an exception chain in the ComputationResult.
            3.  Otherwise, cast the build product, then send in the success result.
        Args:
            request: AxisMappingRequest
        Returns:
            ComputationResult[Vector]
        Raises:
             AxisNodeStepFunctionException
        """
        method = f"{self.__class__.__name__}.next"
        
        # Handle the case that the argument is not safe to use.
        
        previous = request.node
        delta = request.delta
        u = previous.content
        
        if u is None:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                AxisNodeStepFunctionException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisNodeStepFunctionException.MSG,
                    err_code=AxisNodeStepFunctionException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=VectorNullException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorNullException.MSG,
                        err_code=VectorNullException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ),
                ),
            )
        computation = self.compute.addition.execute(
            request=VectorAdditionRequest(
                u=u,
                v=delta,
                id=IdFactory.next_id(class_name="Request")
            )
        )
        # Handle the case that the request is not granted.
        if computation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                AxisNodeStepFunctionException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisNodeStepFunctionException.MSG,
                    err_code=AxisNodeStepFunctionException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=computation.exception,
                ),
            )
        v = cast(Vector, computation.payload)
        node = VectorNode(content=v, previous=previous)
        previous.next = node
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(node)