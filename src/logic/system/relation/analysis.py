# src/logic/system/relation/analysis/analyzer.py

"""
Module: logic.system.relation.analysis.analyzer
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from logic.system import LoggingLevelRouter, RelationReport


P = TypeVar("P")
S = TypeVar("S")

class RelationAnalysis(ABC, Generic[P, S]):
    """
    Role:
        - Analysis interface.
        - Process Runner

    Responsibilities:
        1.  Interface for processes that create a RelationReport instance about the candidates.

    Attributes:

    Provides:
        -   execute(candidate_primary: P, candidate_satellite: S, *args, **kwargs) -> RelationReport:

    Super Class:
    """
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, candidate_primary: P, candidate_satellite: S, *args, **kwargs) -> RelationReport:
        pass