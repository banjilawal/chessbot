# src/operation/computation/worker.py

"""
Module: operation.computation.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Optional, TypeVar, cast

from artifcat import ComputationResult
from collection import VectorSet, VectorTree
from domain import Vector, VectorBlueprint
from fabrication import VectorBuilder
from operation import TopologyComputer
from request import ComputationRequest, TraversalTopologyRequest, VectorBuildRequest
from transit import ComputationPermissionDispatcher, VectorCarrier
from util import IdFactory, LoggingLevelRouter

P = TypeVar("P", bound="ComputationPermissionDispatcher")
Q = TypeVar("Q", bound="ComputationRequest")


class TraversalTopologyComputer(TopologyComputer[TraversalTopologyRequest]):
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
    _vector_builder: VectorBuilder
    
    def __init__(
            self, permitter: ComputationPermissionDispatcher,
            vector_builder: Optional[VectorBuilder] | None = None,
    ):
        """
        Args:
            permitter: ComputationPermissionDispatcher
        """
        super().__init__(permitter=permitter)
        self._vector_builder = vector_builder or VectorBuilder()
        
    @property
    def vector_builder(self) -> VectorBuilder:
        return self._vector_builder
    
    @property
    def permitter(self) -> ComputationPermissionDispatcher:
        return cast(ComputationPermissionDispatcher, super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: TraversalTopologyRequest) -> ComputationResult[VectorTree]:
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
                TopologyGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TopologyGeneratorException.MSG,
                    err_code=TopologyGeneratorException.ERR_CODE,
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
                TopologyGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TopologyGeneratorException.MSG,
                    err_code=TopologyGeneratorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=basis_validation.exception,
                ),
            )
        origin = request.origin
        traversals = request.traversals
        root = cast(Vector, origin_validation.content)
        traversals = cast(VectorSet, basis_validation.authorization_applicant)
        
        solutions = []
        
        for traversal in traversals.iterator:
            x = origin.x + traversal.x
            y = origin.y + traversal.y
            
            computation = self.vector_builder.execute(
                request=VectorBuildRequest(
                    item=VectorCarrier(blueprint=VectorBlueprint(x=x, y=y)),
                    id=IdFactory.next_id(class_name="Request")
                )
            )
            # Handle the case that a solution is not computed.
            if computation.is_failure:
                # Send an exception chain in the result.
                return ComputationResult.failure(
                    TopologyGeneratorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TopologyGeneratorException.MSG,
                        err_code=TopologyGeneratorException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=computation.exception,
                    ),
                )
            solutions.append(cast(Vector, computation.payload))
        vector_set = VectorSet(tuple(solutions))
        tree = VectorTree(root=origin, branches=[vector_set])
        # --- Send the work product. ---#
        return ComputationResult.success(tree)