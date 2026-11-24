# src/topology/generator/math.py

"""
Module: topology.generator.math
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ComputationResult
from collection import VectorChain
from controller import VectorComputationController
from domain import VectorNode
from fabrication import VectorBuilder
from operation import Computer
from request import ProjectionRequest, VectorNodeSequencePermissionRequest, VectorNodeSequenceRequest
from transit import ComputationPermissionDispatcher

from util import IdFactory, LoggingLevelRouter


class VectorNodeSequencer(Computer[VectorNodeSequenceRequest]):
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
            permitter: ComputationPermissionDispatcher,
            vector_builder: Optional[VectorBuilder] | None = None,
            compute: Optional[VectorComputationController] | None = None,
    ):
        """
        Args:
            vector_builder: Optional[VectorBuilder]
            compute: Optional[VectorComputationController]
        """
        super().__init__(permitter=permitter)
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
        
        # --- Get work authorization. ---#
        decision = self.permitter.execute(
            candidate=VectorNodeSequencePermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="Request")
            )
        )
        # Handle the case that the request is not authorized.
        if decision.request_is_denied:
            return ComputationResult.failure(
                VectorNodeSequencerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSequencerException.MSG,
                    err_code=VectorNodeSequencerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        transaction_request = cast(VectorNodeSequenceRequest, decision.transaction_request)

        # --- Extract the transaction participants. ---#
        origin = transaction_request.origin
        cursor = transaction_request.origin
        terminus = transaction_request.terminus
        step_function = transaction_request.step_function
        
        # --- Cast the validation product and setup for the iteration. ---#
        counter = 0
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
                    VectorNodeSequencerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorNodeSequencerException.MSG,
                        err_code=VectorNodeSequencerException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=step.exception,
                    ),
                )
            cursor = cast(VectorNode, step.payload)
            counter = counter + 1
        # --- Perform transaction and state management work. ---#
        chain = VectorChain()
        origin.previous = chain.head
        cursor.next = chain.tail
        chain.head.next = origin
        chain.tail.previous = cursor
        chain.size = counter
        
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(chain)