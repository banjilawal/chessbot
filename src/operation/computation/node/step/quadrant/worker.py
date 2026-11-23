# src/operation/computation/node/step/quadrant/worker.py

"""
Module: operation.computation.node.step.quadrant.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ComputationResult
from domain import Vector, VectorBlueprint, VectorNode
from operation import SpaceNodeStepper
from request import ProjectionRequest, QuadrantProjectionRequest, VectorBuildRequest

from transit import VectorCarrier

from util import IdFactory, LoggingLevelRouter



class QuadrantNodeStepper(SpaceNodeStepper[QuadrantProjectionRequest]):
    """
    Role:
        - Computation

    Responsibilities:
        1.  Get the next vector, V, after U in Quadrant Space, using the linear functions:
                - V.x = U.x + x_step
                - V.y = (2 * slope * U.y) + slope

    Attributes:
        slope: int
        x_step: int

    Provides:
        def next(self, vector: Vector) -> ComputationResult[Vector]

    Super Class:
        SpaceNodeStepper
    """
    _slope: int
    _x_step: int

    
    def __init__(self, slope:int, x_step: int,):
        """
        Args:
            slope: int
            x_step: int
        """
        super().__init__()
        self._slope = slope
        self._x_step = x_step
        
    @property
    def slope(self) -> int:
        return self._slope
    
    @property
    def x_step(self) -> int:
        return self._x_step

    @LoggingLevelRouter.monitor
    def execute(self, request: ProjectionRequest) -> ComputationResult[VectorNode]:
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
             QuadrantNodeStepperException
        """
        method = f"{self.__class__.__name__}.next"
        
        # Handle the case that the argument is not safe to use.
        validation = self.math.origin.validator.execute(vector)
        if validation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                QuadrantNodeStepperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantNodeStepperException.MSG,
                    err_code=QuadrantNodeStepperException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=validation.exception,
                ),
            )
        previous = request.node
        
        u = previous.content
        if u is None:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                QuadrantNodeStepperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantNodeStepperException.MSG,
                    err_code=QuadrantNodeStepperException.ERR_CODE,
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
        x = u.x + self.x_step
        y = (2 * u.y * self.slope) + self.slope
        
        build = self.vector_builder.execute(
            request=VectorBuildRequest(
                item=VectorCarrier(blueprint=VectorBlueprint(x=x, y=y)),
                id=IdFactory.next_id(class_name="Request")
            )
        )
        # Handle the case that the build is not successful.
        if build.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                QuadrantNodeStepperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantNodeStepperException.MSG,
                    err_code=QuadrantNodeStepperException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=build.exception,
                ),
            )
        v = cast(Vector, build.payload)
        node = VectorNode(content=v, previous=previous)
        previous.next = node
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(node)