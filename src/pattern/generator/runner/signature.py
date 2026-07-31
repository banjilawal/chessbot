# src/pattern/generator/runner/pattern.py

"""
Module: pattern.generator.runner.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import  annotations

from typing import List, Optional, Type, cast

from container import VectorSet
from err import TopologyGeneratorException
from geometry import RecurrenceRegistry
from math import VectorSequenceGenerator

from result import ComputationResult, MethodResultType
from util import LoggingLevelRouter
from validator import PrimingValidator



class TransformerRunner:
    """
    Role:
        -   Computation

    Responsibilities:
        1.  Generate a Bishop's diagonal traversal patterns.

    Attributes:
        math_toolkit: Optional[MathToolkit]
        vector_sequence_generator: Optional[VectorSequenceGenerator]

    Provides:
        def execute(recurrence_table: QuadrantRecurrenceTable) -> ComputationResult[List[VectorSet]]

    Super Class:
        SpaceMappingFunction
    """
    _priming_validator: PrimingValidator
    _vector_sequence_generator: VectorSequenceGenerator
    
    def __init__(
            self,
            priming_validator: Optional[PrimingValidator] | None = PrimingValidator(),
            vector_sequence_generator: Optional[VectorSequenceGenerator] | None = VectorSequenceGenerator(),
    ):
        """
        Args:
            priming_validator: Optional[PrimingValidator]
            sequence_generator: Optional[VectorSequenceGenerator]
        """
        self._priming_validator = priming_validator
        self._vector_sequence_generator = vector_sequence_generator
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @property
    def vector_sequence_generator(self) -> VectorSequenceGenerator:
        return self._vector_sequence_generator
    

    @LoggingLevelRouter.monitor
    def execute(
            self,
            recurrence_registry_model: Type[RecurrenceRegistry],
            recurrence_registry: RecurrenceRegistry,
    ) -> ComputationResult[List[VectorSet]]:
        method = f"{self.__class__.__name__}.execute"
        
        registry = cast(recurrence_registry_model, recurrence_registry)
        recurrences = registry.type_recurrence_dict
        
        solution_sets: [VectorSet] = []
        for model in recurrences.keys():
            recurrence = cast(model, recurrences[model])
            computation = self._vector_sequence_generator.execute(
                recurrence=recurrence
            )
            if computation.is_failure:
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
            solution_sets.append(cast(VectorSet, computation.payload))
        return ComputationResult.success(solution_sets)
        
            