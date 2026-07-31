# src/pattern/generator/pattern.py

"""
Module: pattern.generator.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import  annotations

from typing import Optional, Type, TypeVar, cast

from container import VectorSet, VectorTree
from err import TopologyGeneratorException, RecurrenceRegistryCollectionNullException
from geometry import RecurrenceRegistryCollection
from pattern import TransformerRunner

from result import ComputationResult, MethodResultType

from topology import Topology
from util import LoggingLevelRouter
from validator import PrimingValidator

T = TypeVar("T", bound="TraversalRank")

class TraversalTopologyGenerator:
    """
    Role:
        -   Computation

    Responsibilities:
        1.  Generate a Bishop's diagonal traversal patterns.

    Attributes:
        math_toolkit: Optional[MathToolkit]
        transformer_runner: Optional[TransformerRunner]

    Provides:
        def execute(recurrence_table: QuadrantRecurrenceTable) -> ComputationResult[List[VectorSet]]

    Super Class:
        SpaceMappingFunction
    """
    _priming_validator: PrimingValidator
    _transformer_runner: TransformerRunner
    
    def __init__(
            self,
            priming_validator: Optional[PrimingValidator] | None = PrimingValidator(),
            transformer_runner: Optional[TransformerRunner] | None = TransformerRunner(),
    ):
        """
        Args:
            priming_validator: Optional[PrimingValidator]
            transformer_runner: Optional[TransformerRunner]
        """
        self._priming_validator = priming_validator
        self._transformer_runner =transformer_runner
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @property
    def transformer_runner(self) -> TransformerRunner:
        return self._transformer_runner
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            collection: RecurrenceRegistryCollection
    ) -> ComputationResult[Topology]:
        """
        Generate the set of vectors in a Bishop's traversal pattern.

        Action:
            1.  Send an exception chain in the ComputationResult if either.
                    -   The recurrence_table fails a validation check,
                    -   A computation fails.
            2.  Otherwise, send the solutions in the success result.
        Args:
             collection: RecurrenceTableGroup
        Returns:
            ComputationResult[List[VectorSet]]
        Raises:
            BishopPatternGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Cast the validation product and setup for the iteration. ---#
        validation = self._priming_validator.execute(
            candidate=collection,
            target=Type[RecurrenceRegistryCollection],
            null_exception=RecurrenceRegistryCollectionNullException(),
        )
        if validation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                TopologyGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TopologyGeneratorException.MSG,
                    err_code=TopologyGeneratorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=validation.exception,
                ),
            )
        collection = cast(RecurrenceRegistryCollection, validation.payload)
        registry_dict = collection.recurrence_registry_type_dict
        
        solution_sets = []
        # --- Process each recurrence_table ---#
        for registry_class in registry_dict.keys():
            computation = self._transformer_runner.execute(
                registry_class=registry_class,
                recurrence_registry=registry_dict[registry_class],
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
            # Otherwise, add to solution set
            solution_sets.append(cast([VectorSet], computation.payload))
        origin = collection.origin
        tree = VectorTree(root=origin, branches=solution_sets)
        # --- Send the work product. ---#
        return ComputationResult.success(Topology(tree=tree))
        
            