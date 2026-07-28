# src/pattern/generator/pattern.py

"""
Module: pattern.generator.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import  annotations

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from container import VectorSet
from math import VectorSequenceGenerator
from recurrence import RecurrenceTable
from result import ComputationResult
from util import LoggingLevelRouter
from validator import PrimingValidator

T = TypeVar("T", bound="Rank")

class PatternGenerator(ABC, Generic[T]):
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
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, recurrence_table: RecurrenceTable) -> ComputationResult[List[VectorSet]]:
        pass
