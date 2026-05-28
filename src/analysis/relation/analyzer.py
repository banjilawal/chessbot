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

from analysis import Analyzer
from report import RelationReport
from result import AnalysisResult
from util import LoggingLevelRouter

P = TypeVar("P")
S = TypeVar("S")

class RelationAnalyzer(Analyzer[RelationReport], Generic[P, S]):
    """
    Role:
        - Analyst interface.
        - Process Runner

    Responsibilities:
        1.  Interface for processes that create a RelationReport instance about the candidates.

    Attributes:

    Provides:
        -   analyze(
                    candidate_primary: P,
                    candidate_satellite: S,
                    *args,
                    **kwargs,
            ) -> AnalysisResult[RelationReport]:

    Super Class:
    """
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            candidate_primary: P,
            candidate_satellite: S,
            *args,
            **kwargs,
    ) -> AnalysisResult[RelationReport]:
        pass