# src/operation/computation/topology/traversal/rook/worker.py

"""
Module: operation.computation.topology.traversal.rook.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, cast

from artifcat import ComputationResult
from collection import VectorChain, VectorTree
from operation import TraversalTopologyComputer
from request import RookTopologyPermissionRequest, RookTopologyRequest
from transit import ComputationPermissionDispatcher
from util import IdFactory, LoggingLevelRouter


class RookTopologyComputer(TraversalTopologyComputer[RookTopologyRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a ComputationRequest

    Attributes:
        permitter: ComputationPermissionDispatcher
        
    Provides:
        -   def execute(request: RookTopologyRequest) -> ComputationResult[VectorTree]

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
    def execute(self, request: RookTopologyRequest) -> ComputationResult[VectorTree]:
        """
        Generate the set of vectors in a Rook's traversal basis.

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
            RookBasisGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Get work authorization. ---#
        decision = self.permitter.execute(
            candidate=RookTopologyPermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="Request")
            )
        )
        # Handle the case that the request is not authorized.
        if decision.request_is_denied:
            return ComputationResult.failure(
                RookTopologyComputerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RookTopologyComputerException.MSG,
                    err_code=RookTopologyComputerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        transaction_request = cast(RookTopologyRequest, decision.transaction_request)
        
        # --- Extract the transaction participants. ---#
        origin = transaction_request.origin
        branches: List[VectorChain] = []
        
        # --- Perform transaction and state management work. ---#
        for job in request.sequence_requests:
            work = self.sequencer.execute(request=job)
            if work.is_failure:
                # Send an exception chain in the result.
                return ComputationResult.failure(
                    RookTopologyComputerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RookTopologyComputerException.MSG,
                        err_code=RookTopologyComputerException.ERR_CODE,
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