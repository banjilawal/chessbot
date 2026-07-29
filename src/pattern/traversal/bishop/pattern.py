# src/pattern/traversal/bishop/pattern.py

"""
Module: pattern.traversal.bishop.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from typing import List, Optional, Tuple, Type, cast

from container import VectorSet
from err import BishopTraversalPatternException
from err.null.recurrence.group import BishopRecurrenceSeriesNullException
from model import Bishop
from pattern import PatternGenerator, TraversalPattern
from recurrence import BishopRecurrenceSets
from result import ComputationResult
from util import LoggingLevelRouter
from validator import PrimingValidator


class BishopPattern(TraversalPattern[Bishop]):
    
    def __init__(
            self,
            priming_validator: Optional[PrimingValidator],
            pattern_generator: Optional[PatternGenerator],
    ):
        """
        Args:
            pattern_generator: Optional[PatternGenerator]
        """
        super().__init__(pattern_generator=pattern_generator, priming_validator=priming_validator)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            recurrence_table_group: BishopRecurrenceSets
    ) -> ComputationResult[Tuple[VectorSet]]:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the recurrence_table_group is not safe to use.
        validation = self.priming_validator.execute(
            candidate=recurrence_table_group,
            target_model=Type[BishopRecurrenceSets],
            null_exception=BishopRecurrenceSeriesNullException(),
        )
        if validation.is_failure:
            # Send the exception chain in the result.
            return ComputationResult.failure(
                BishopTraversalPatternException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BishopTraversalPatternException.MSG,
                    err_code=BishopTraversalPatternException.ERR_CODE,
                    ex=validation.exception
                )
            )
        # Cast the validation product for additional processing.
        recurrence_tables = cast(BishopRecurrenceSets, validation.payload)
        
        computation = self.pattern_generator.execute(
            recurrence_table_group=recurrence_tables
        )
        # Handle the case that the computation does not produce a result.
        if computation.is_failure:
            # Send the exception chain in the result.
            return ComputationResult.failure(
                BishopTraversalPatternException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BishopTraversalPatternException.MSG,
                    err_code=BishopTraversalPatternException.ERR_CODE,
                    ex=validation.exception
                )
            )
        pattern = cast(Tuple[VectorSet], computation.payload)
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(pattern)