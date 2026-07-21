# src/space/ruleset/space.py

"""
Module: space.ruleset.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Dict, Generic, List, Optional, TypeVar, cast

from model import TargetVectorSet, Vector
from result import ComputationResult
from space import TraversalPattern
from util import LoggingLevelRouter

T = TypeVar("T", bound="Rank")

class TraversalRuleset(ABC, Generic[T]):
    """
    Role:
        -   Dataset

    Responsibilities:
        1. Collect of traversal patterns for a rank

    Attributes:
        size: int
        is_empty: bool
        is_not_empty: bool
        entries: Dict[str: TraversalPattern]
        to_list: List[TraversalPattern]:

    Provides:

    Super Class:
    """
    _ruleset: Dict[str: TraversalPattern]
    
    def __init__(
            self,
            entries: Optional[Dict[str: TraversalPattern]] | None = None
    ):
        """
        Args:
            entries: Optional[Dict[str: TraversalPattern]]
        """
        self._ruleset = entries or {}
        
    @property
    def ruleset(self) -> Dict[str: TraversalPattern]:
        return self._ruleset
    
    @property
    def size(self) -> int:
        return len(self._ruleset)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def to_list(self) -> List[TraversalPattern]:
        return list(self._ruleset)
    
    @LoggingLevelRouter.monitor
    def execute(self, origin: Vector) -> ComputationResult[TargetVectorSet]:
        for rule in self.ruleset.entries:
            for entry in rule
        