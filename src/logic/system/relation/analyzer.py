# src/logic/system/relation/analysis/analyzer.py

"""
Module: logic.system.relation.analysis.analyzer
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from logic.system import LoggingLevelRouter, RelationReport


P = TypeVar("P")
S = TypeVar("S")

class RelationAnalyzer(ABC, Generic[P, S]):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def analyze(cls, candidate_primary: P, candidate_satellite: S) -> RelationReport[P, S]:
        pass