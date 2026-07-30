# src/builder/pattern/generator/ruleset/builder/pattern.py

"""
Module: builder.pattern.generator.ruleset.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, List, TypeVar

from model import Rank
from recurrence import RecurrenceRegistry

T = TypeVar("T", bound="Rank")

class PatternGenerationRuleset(ABC, Generic[T]):
    _rank: T
    _recurrence_tables: List[RecurrenceRegistry]
    
    def __init__(self, rank: Rank, recurrence_tables: List[RecurrenceRegistry]):
        """
        Args:
            rank: Rank
            recurrence_tables: List[RecurrenceTable]
        """
        self._rank = rank
        self._recurrence_tables = recurrence_tables
        
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def recurrence_tables(self) -> List[RecurrenceRegistry]:
        return self._recurrence_tables