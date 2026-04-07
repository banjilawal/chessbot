# src/analyst/relation/analyst.py

"""
Module: analyst.relation.analyst
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from abc import abstractmethod
from typing import Generic, TypeVar

from analyst import Analyst
from model import RelationReport
from result import AnalysisResult
from system import LoggingLevelRouter


P = TypeVar("P")
S = TypeVar("S")

class RelationAnalyst(Analyst[S], Generic[P, S]):
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
    def analyze(
            cls,
            candidate_primary: P,
            candidate_satellite: S,
            *args, **kwargs
    ) -> AnalysisResult[RelationReport]:
        pass