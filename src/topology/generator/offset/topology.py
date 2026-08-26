# src/topology/generator/offset/topology.py

"""
Module: topology.generator.offset.topology
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, TypeVar, cast

from collection import VectorSet, VectorTree
from err import TopologyGeneratorException, VectorSetNullException
from domain.model import Vector
from artifcat import ComputationResult, MethodResultType
from operation.toolkit import MathToolkit
from topology import Topology
from util import LoggingLevelRouter
from transit.dispatcher.validator import PrimingValidator

T = TypeVar("T", bound="OffsetRank")


class OffsetTopologyGenerator:
    """
    Role:
        -   Computation

    Responsibilities:
        1.  Generate a Bishop's diagonal traversal basiss.

    Attributes:
        math_toolkit: Optional[MathToolkit]
        priming_validator: Optional[PrimingValidator]

    Provides:
        def execute(recurrence_table: QuadrantRecurrenceTable) -> ComputationResult[List[VectorSet]]

    Super Class:
        SpaceMappingFunction
    """
    _math_toolkit: MathToolkit
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            math_toolkit: Optional[MathToolkit] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            math_toolkit: Optional[MathToolkit]
            priming_validator: Optional[PrimingValidator]
        """
        self._math_toolkit = math_toolkit or MathToolkit()
        self._priming_validator = priming_validator or PrimingValidator()
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            origin: Vector,
            basis_vectors: VectorSet
    ) -> ComputationResult[Topology]:
        """
        Generate the set of vectors in a Bishop's traversal basis.

        Action:
            1.  Send an exception chain in the ComputationResult if either.
                    -   The recurrence_table fails a validation check,
                    -   A computation fails.
            2.  Otherwise, send the solutions in the success result.
        Args:
             basis: OffsetTopologyBasis
        Returns:
            ComputationResult[List[VectorSet]]
        Raises:
            BishopBasisGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the origin is not safe to use.
        origin_validation = self._math_toolkit.vector.validator.execute(candidate=origin)
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
        # Handle the case that, the basis is not valid.
        basis_validation = self._priming_validator.execute(
            candidate=basis_vectors,
            target=Type[VectorSet],
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
        root = cast(Vector, origin_validation.payload)
        offsets = cast(VectorSet, basis_validation.payload)
        
        solutions = []
        for offset in offsets.iterator:
            computation = self._math_toolkit.add_vector.execute(
                u=origin,
                v=offset
            )
            # Handle the case that, a solution is not computed.
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
        return ComputationResult.success(Topology(tree=tree))

