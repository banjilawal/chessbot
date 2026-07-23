# src/space/ruleset/space.py

"""
Module: space.ruleset.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Dict, Generic, List, TypeVar

from space import TraversalPattern

T = TypeVar("T", bound="Rank")

class TraversalRuleset(ABC, Generic[T]):
    """
    Role:
        -   Data Holder
        -   Immutability

    Responsibilities:
        1.  Determine potential destinations from Token's current position using
            a set of TraversalPatterns.

    Attributes:
        rule_count: int
        is_empty: bool:
        is_not_empty: bool
        to_list: List[TraversalPattern]
        ruleset: Dict[str: TraversalPattern]


    Provides:

    Super Class:
    """
    _ruleset: Dict[str: TraversalPattern]
    
    def __init__(self, ruleset: Dict[str: TraversalPattern]):
        """
        Args:
            rulesets: Dict[str: TraversalPattern]
        """
        self._ruleset = ruleset
        
    @property
    def ruleset(self) -> Dict[str: TraversalPattern]:
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
    
    @property
    def to_list(self) -> List[TraversalPattern]:
        return list(self._ruleset)
        