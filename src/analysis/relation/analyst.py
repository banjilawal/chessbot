# src/analysis/relation/analyst.py

"""
Module: analysis.relation.analyst
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from abc import abstractmethod
from typing import Generic, TypeVar

from analysis import Analyst
from report import RelationReport
from result import AnalysisResult
from system import LoggingLevelRouter


P = TypeVar("P")
S = TypeVar("S")

class RelationAnalyst(Analyst[RelationReport], Generic[P, S]):
    """
    Role:
        - Analyst interface.
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
    def analyze(
            cls,
            candidate_primary: P,
            candidate_satellite: S,
            *args, **kwargs
    ) -> AnalysisResult[RelationReport]:
        pass