# src/operation/computation/topology/traversal/queen/worker.py

"""
Module: operation.computation.topology.traversal.queen.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, cast

from artifcat import ComputationResult
from collection import VectorChain, VectorTree
from operation import TraversalTopologyComputer
from request import QueenTopologyRequest
from transit import ComputationPermissionDispatcher
from util import IdFactory, LoggingLevelRouter


class QueenTopologyComputer(TraversalTopologyComputer[QueenTopologyRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a ComputationRequest

    Attributes:
        permitter: ComputationPermissionDispatcher
        
    Provides:
        -   def execute(request: QueenTopologyRequest) -> ComputationResult[VectorTree]

    Super Class:
        TraversalTopologyComputer
    """
    
    def __init__(
            self, permitter: ComputationPermissionDispatcher,
    ):
        """
        Args:
            permitter: ComputationPermissionDispatcher
        """
        super().__init__(permitter=permitter)
    
    @property
    def permitter(self) -> ComputationPermissionDispatcher:
        return cast(ComputationPermissionDispatcher, super().permitter)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: QueenTopologyRequest) -> ComputationResult[VectorTree]:
        """
        Generate the set of vectors in a Queen's traversal basis.

        Action:
            1.  Send an exception chain in the ComputationResult if either.
                    - The recurrence_table fails a validation check,
                    - A computation fails.
            2.  Otherwise, send the solutions in the success result.
        Args:
             request: TraversalTopologyRequest
        Returns:
            ComputationResult[List[VectorSet]]
        Raises:
            QueenBasisGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Get work authorization. ---#
        decision = self.permitter.execute(
            candidate=QueenTopologyPermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="Request")
            )
        )
        # Handle the case that the request is not authorized.
        if decision.request_is_denied:
            return ComputationResult.failure(
                QueenTopologyComputerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QueenTopologyComputerException.MSG,
                    err_code=QueenTopologyComputerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        transaction_request = cast(QueenTopologyRequest, decision.transaction_request)
        
        # --- Extract the transaction participants. ---#
        origin = transaction_request.origin
        branches: List[VectorChain] = []
        
        # --- Perform transaction and state management work. ---#
        for job in request.sequence_requests:
            work = self.sequencer.execute(request=job)
            if work.is_failure:
                # Send an exception chain in the result.
                return ComputationResult.failure(
                    QueenTopologyComputerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=QueenTopologyComputerException.MSG,
                        err_code=QueenTopologyComputerException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=work.exception,
                    ),
                )
            # --- Iteration completed. ---#
            chain = cast(VectorChain, work.payload)
            branches.append(chain)
        tree = VectorTree(root=origin, branches=branches)
        # --- Send the work product. ---#
        return ComputationResult.success(tree)
