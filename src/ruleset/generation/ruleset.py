# src/ruleset/generation/ruleset.py

"""
Module: ruleset.generation.ruleset
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Tuple, TypeVar

from ruleset import SequenceSpec

T = TypeVar("T", bound="Rank")


class PatternGenerationRuleset(ABC, Generic[T]):
    _ruleset: Tuple[SequenceSpec, ...]
    
    def __init__(self, ruleset: Tuple[SequenceSpec, ...]):
        self._ruleset = ruleset
        
    @property
    @abstractmethod
    def ruleset(self) -> Tuple[SequenceSpec, ...]:
        return self._ruleset
    
    @property
    def rule_count(self) -> int:
        return len(self._ruleset)
    
    @property
    def is_empty(self) -> bool:
        return self.rule_count == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
        
    