# src/movement/generator/bishop/pattern.py

"""
Module: movement.generator.bishop.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, Type, cast

from container import VectorSet
from err import NullException
from math import VectorSequenceGenerator
from recurrence import QuadrantRecurrenceTable
from result import ComputationResult, MethodResultType
from toolkit import MathToolkit

from util import LoggingLevelRouter
from validator import PrimingValidator


class BishopVectorSetGenerator:
    _math: MathToolkit
    _sequence_generator: VectorSequenceGenerator
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            math_toolkit: Optional[MathToolkit] | None = MathToolkit(),
            priming_validator: Optional[PrimingValidator] | None = PrimingValidator(),
            vector_sequence_generator:  Optional[VectorSequenceGenerator] | None = VectorSequenceGenerator(),
    ):
        """
        Args:
            math_toolkit: Optional[MathToolkit]
            vector_sequence_generator: Optional[BishopPatternGenerator]
        """
        self._math = math_toolkit
        self._priming_validator = priming_validator
        self.sequence_generator = vector_sequence_generator
        
    
    @LoggingLevelRouter.monitor
    def execute(self, recurrence_table: QuadrantRecurrenceTable) -> ComputationResult[List[VectorSet]]:
        method = f"{self.__class__.__name__}.execute"
        
        validation = self._priming_validator.execute(
            candidate=recurrence_table,
            target=Type[QuadrantRecurrenceTable],
            null_exception=NullException(),
        )
        if validation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                BishopPatternGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BishopPatternGeneratorException.MSG,
                    err_code=BishopPatternGeneratorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=validation.exception,
                ),
            )
        # --- Cast the validation product and setup for the iteration. ---#
        recurrences  = cast(QuadrantRecurrenceTable, validation.payload)
        vector_sets: List[VectorSet] = []
        
        for key in recurrences.type_recurrence_dict:
            recurrence = cast(key, recurrences[key])
            computation = self._sequence_generator.execute(recurrence)
            
            if computation.is_failure:
                # Send an exception chain in the result.
                return ComputationResult.failure(
                    BishopPatternGeneratorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BishopPatternGeneratorException.MSG,
                        err_code=BishopPatternGeneratorException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=validation.exception,
                    ),
                )
            vector_sets.append(cast(VectorSet, computation.payload))
        return ComputationResult.success(vector_sets)

        
        
    