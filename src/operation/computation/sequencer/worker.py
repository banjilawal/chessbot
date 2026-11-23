# src/topology/generator/math.py

"""
Module: topology.generator.math
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from collection import VectorChain, VectorSet
from controller import VectorComputationController
from domain import VectorNode
from domain.model import Vector
from fabrication import VectorBuilder
from request import ProjectionRequest, VectorNodeSequenceRequest
from surface.topology.recurrence import Recurrence
from artifcat import ComputationResult

from util import IdFactory, LoggingLevelRouter


class VectorNodeSequencer:
    """
    Role:
        - Computation
        - Integrity Assurance

    Responsibilities:
        Define x_step and slope for getting the next vector northeast of origin.
            - x_step = -1,
            - slope = 1

    Attributes:
        vector_builder: VectorBuilder
        compute: VectorComputationController

    Provides:
        -   def execute(specification: Recurrence) -> ComputationResult[VectorSet]
        
    Super Class:
        Computer
    """
    
    _vector_builder: VectorBuilder
    _compute: VectorComputationController
    
    def __init__(
            self,
            vector_builder: Optional[VectorBuilder] | None = None,
            compute: Optional[VectorComputationController] | None = None,
    ):
        """
        Args:
            vector_builder: Optional[VectorBuilder]
            compute: Optional[VectorComputationController]
        """
        self._vector_builder = vector_builder or VectorBuilder()
        self._compute = compute or VectorComputationController()
    
    @property
    def vector_builder(self) -> VectorBuilder:
        return self._vector_builder
    
    @property
    def compute(self) -> VectorComputationController:
        return self._compute
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: VectorNodeSequenceRequest) -> ComputationResult[VectorChain]:
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
            request: VectorNodeSequenceRequest
        Returns:
            ComputationResult[VectorChain]
        Raises:
             AxisMappingException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the sequence gets flagged,
        validation = self._math.priming_validator.execute(
            request=recurrence,
            target_model=Recurrence,
            null_exception=RecurrenceNullException(),
        )
        if validation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                VectorSequenceGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorSequenceGeneratorException.MSG,
                    err_code=VectorSequenceGeneratorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=validation.exception,
                ),
            )
        # --- Cast the validation product and setup for the iteration. ---#
        origin = request.origin
        cursor = request.origin
        terminus = request.terminus
        step_function = request.step_function
        
        while cursor.content != terminus:
            step = step_function.execute(
                request=ProjectionRequest(
                    node=cursor,
                    id=IdFactory.next_id(class_name="Request")
                )
            )
            if step.is_failure:
                # Send an exception chain in the result.
                return ComputationResult.failure(
                    VectorSequenceGeneratorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorSequenceGeneratorException.MSG,
                        err_code=VectorSequenceGeneratorException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=step.exception,
                    ),
                )
            cursor = cast(VectorNode, step.payload)
        chain = VectorChain(head=origin, tail=cursor)
            

            
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(chain)
        