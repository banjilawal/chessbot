# src/builder/pattern/generator/bishop/builder/pattern.py

"""
Module: builder.pattern.generator.bishop.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, Type, cast

from container import VectorSet
from err import BishopPatternGeneratorException, QuadrantRecurrenceTableNullException
from math import VectorSequenceGenerator
from model import Bishop
from pattern import PatternGenerator
from recurrence import QuadrantRecurrenceTable
from result import ComputationResult, MethodResultType

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
            priming_validator: Optional[PrimingValidator]
            vector_sequence_generator: Optional[BishopPatternGenerator]
        """
        super().__init__(
            priming_validator=priming_validator,
            vector_sequence_generator=vector_sequence_generator
        )

        
        
    