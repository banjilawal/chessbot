# src/sequence/generator/bishop/sequence.py

"""
Module: sequence.generator.bishop.sequence
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, cast

from container import VectorSet
from recurrence.table.quadrant.recurrence import QuadrantRecurrenceTable
from result import ComputationResult
from toolkit import MathToolkit
from util import LoggingLevelRouter


class BishopPatternGenerator:
    _math: MathToolkit
    _sequence_generator: BishopPatternGenerator
    
    def __init__(
            self, 
            math_toolkit: Optional[MathToolkit] | None = MathToolkit(),
            vector_sequence_generator:  Optional[BishopPatternGenerator] | None = BishopPatternGenerator(),
    ):
        """
        Args:
            math_toolkit: Optional[MathToolkit]
            vector_sequence_generator: Optional[BishopPatternGenerator]
        """
        self._math = math_toolkit
        self.sequence_generator = vector_sequence_generator
        
        
    
    @LoggingLevelRouter.monitor
    def execute(self, recurrence_table: QuadrantRecurrenceTable) -> ComputationResult[List[VectorSet]]:
        method = f"{self.__class__.__name__}.execute"
        
        validation = recurrence_table_validator.execute(recurrence_table)
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
        recurrences  = cast(Recurrence, validation.payload)
        solutions: List[VectorSet] = []
        
        computation = self.sequence_generator.execute(recurrences.northeast)
        if computation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                BishopPatternGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BishopPatternGeneratorException.MSG,
                    err_code=BishopPatternGeneratorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=computation.exception,
                ),
            )
        solutions.append(cast(VectorSet, computation.payload))


        computation = self.sequence_generator.execute(recurrences.northwest)
        if computation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                BishopPatternGeneratorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BishopPatternGeneratorException.MSG,
                    err_code=BishopPatternGeneratorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=computation.exception,
                ),
            )
        solutions.append(cast(VectorSet, computation.payload))
    