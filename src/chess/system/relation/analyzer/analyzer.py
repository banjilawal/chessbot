# src/chess/system/relation/__init__.py

"""
Module: chess.system.relation.__init__
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system import LoggingLevelRouter, RelationReport


P = TypeVar("P")
S = TypeVar("S")

class RelationAnalyzer(ABC, Generic[P, S]):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def analyze(cls, candidate_primary: P, candidate_satellite: S) -> RelationReport[P, S]:
        pass