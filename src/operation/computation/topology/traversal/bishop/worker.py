# src/operation/computation/topology/traversal/bishop/worker.py

"""
Module: operation.computation.topology.traversal.bishop.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, cast

from artifcat import ComputationResult
from collection import VectorChain, VectorTree
from operation import TraversalTopologyComputer
from request import BishopTopologyRequest
from transit import ComputationPermissionDispatcher
from util import LoggingLevelRouter


class BishopTopologyComputer(TraversalTopologyComputer[BishopTopologyRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a ComputationRequest

    Attributes:
        vector_builder: VectorBuilder
        permitter: ComputationPermissionDispatcher
        
    Provides:
        -   def execute(request: Q) -> ComputationResult

    Super Class:
        Worker
    """
    
    def __init__(
            self, permitter: ComputationPermissionDispatcher,
            vector_builder: Optional[VectorBuilder] | None = None,
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
    def execute(self, request: BishopTopologyRequest) -> ComputationResult[VectorTree]:
        """
        Generate the set of vectors in a Bishop's traversal basis.

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
            BishopBasisGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the origin is not safe to use.
        origin_validation = self._math_toolkit.origin.validator.execute(candidate=origin)
        if origin_validation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                BishopTopologyComputerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BishopTopologyComputerException.MSG,
                    err_code=BishopTopologyComputerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=origin_validation.exception,
                ),
            )
        # Handle the case that the basis is not valid.
        basis_validation = self._priming_validator.execute(
            request=basis_vectors,
            candidate=Type[VectorSet],
            null_exception=VectorSetNullException(),
        )
        if basis_validation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                BishopTopologyComputerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BishopTopologyComputerException.MSG,
                    err_code=BishopTopologyComputerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=basis_validation.exception,
                ),
            )
        origin = request.origin
        branches: List[VectorChain] = []
        
        for job in request.sequence_requests:
            work = self.sequencer.execute(request=job)
            if work.is_failure:
                # Send an exception chain in the result.
                return ComputationResult.failure(
                    BishopTopologyComputerException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BishopTopologyComputerException.MSG,
                        err_code=BishopTopologyComputerException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=work.exception,
                    ),
                )
            chain = cast(VectorChain, work.payload)
            branches.append(chain)
        tree = VectorTree(root=origin, branches=branches)
        # --- Send the work product. ---#
        return ComputationResult.success(tree)