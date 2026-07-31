# src/builder/pattern/generator/builder/pattern.py

"""
Module: builder.pattern.generator.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import  annotations

from abc import abstractmethod
from typing import Optional, Tuple, Type, TypeVar, cast

from container import VectorSet
from err import PatternGeneratorException
from err.null.recurrence.group import RecurrenceTableGroupNullException
from pattern import TransformerRunner
from geometry.recurrence import RecurrenceRegistryCollection
from result import ComputationResult, MethodResultType
from util import LoggingLevelRouter
from validator import PrimingValidator

T = TypeVar("T", bound="Rank")

class PatternGenerator:
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
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            recurrence_set: RecurrenceRegistryCollection
    ) -> ComputationResult[Tuple[VectorSet]]:
        """
        Generate the set of vectors in a Bishop's traversal pattern.

        Action:
            1.  Send an exception chain in the ComputationResult if either.
                    -   The recurrence_table fails a validation check,
                    -   A computation fails.
            2.  Otherwise, send the solutions in the success result.
        Args:
             recurrence_set: RecurrenceTableGroup
        Returns:
            ComputationResult[List[VectorSet]]
        Raises:
            BishopPatternGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Cast the validation product and setup for the iteration. ---#
        validation = self._priming_validator.execute(
            candidate=recurrence_set,
            target=Type[RecurrenceRegistryCollection],
            null_exception=RecurrenceTableGroupNullException(),
        )
        if validation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                PatternGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PatternGeneratorException.MSG,
                    err_code=PatternGeneratorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=validation.exception,
                ),
            )
        group = cast(RecurrenceRegistryCollection, validation.payload)
        table_dict = group.recurrence_registry_type_dict
        
        solution_sets = []
        # --- Process each recurrence_table ---#
        for table_type in table_dict.keys():
            computation = self._transformer_runner.execute(
                table_type=table_type,
                recurrence_registry=table_dict[table_type],
            )
            # Handle the case that, a solution is not computed.
            if computation.is_failure:
                # Send an exception chain in the result.
                return ComputationResult.failure(
                    PatternGeneratorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PatternGeneratorException.MSG,
                        err_code=PatternGeneratorException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=computation.exception,
                    ),
                )
            # Otherwise, add to solution set
            solution_sets.append(cast(Tuple[VectorSet], computation.payload))
        # --- Send the work product. ---#
        return ComputationResult.success(solution_sets)
        
            