# src/pattern/generator/bishop/pattern.py

"""
Module: pattern.generator.bishop.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, Type, cast

from container import VectorSet
from err import BishopPatternGeneratorException, QuadrantRecurrenceTableNullException
from math import VectorSequenceGenerator
from recurrence import QuadrantRecurrenceTable
from result import ComputationResult, MethodResultType
from toolkit import MathToolkit

from util import LoggingLevelRouter
from validator import PrimingValidator


class BishopPatternGenerator:
    """
    Role:
        -   Computation

    Responsibilities:
        1.  Generate a Bishop's diagonal traversal patterns.

    Attributes:
        math_toolkit: Optional[MathToolkit]
        vector_sequence_generator: Optional[BishopPatternGenerator]

    Provides:
        def execute(recurrence_table: QuadrantRecurrenceTable) -> ComputationResult[List[VectorSet]]

    Super Class:
        SpaceMappingFunction
    """
    
    def __init__(
            self,
            priming_validator: Optional[PrimingValidator] |
                               None = PrimingValidator(),
            vector_sequence_generator:  Optional[VectorSequenceGenerator] |
                                        None = VectorSequenceGenerator(),
    ):
        """
        Args:
            math_toolkit: Optional[MathToolkit]
            vector_sequence_generator: Optional[BishopPatternGenerator]
        """
        super().__init__(
            priming_validator=priming_validator,
            vector_sequence_generator=vector_sequence_generator
        )
        
    
    @LoggingLevelRouter.monitor
    def execute(self, recurrence_table: QuadrantRecurrenceTable) -> ComputationResult[List[VectorSet]]:
        """
        Generate the set of vectors in a Bishop's traversal pattern.

        Action:
            1.  Send an exception chain in the ComputationResult if either.
                    -   The recurrence_table fails a validation check,
                    -   A computation fails.
            2.  Otherwise, send the solutions in the success result.
        Args:
            recurrence_table: QuadrantRecurrenceTable
        Returns:
            ComputationResult[List[VectorSet]]
        Raises:
            BishopPatternGeneratorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the request cannot get bootstrapped.
        validation = self._priming_validator.execute(
            candidate=recurrence_table,
            target=Type[QuadrantRecurrenceTable],
            null_exception=QuadrantRecurrenceTableNullException(),
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
        solution_sets: List[VectorSet] = []
        
        # --- Process each recurrence ---#
        for key in recurrences.type_recurrence_dict:
            # Compute the set of destinations in the
            recurrence = cast(key, recurrences[key])
            computation = self._sequence_generator.execute(recurrence)
            
            # Handle the case that, a solution is not computed.
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
            # Otherwise, add to solution set
            solution_sets.append(cast(VectorSet, computation.payload))
        # --- Send the work product. ---#
        return ComputationResult.success(solution_sets)

        
        
    