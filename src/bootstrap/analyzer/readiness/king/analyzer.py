# src/bootstrap/analyzer/readiness/king/analyzer.py

"""
Module: bootstrap.analyzer.readiness.king.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analyzer import Analyzer
from model import KingToken
from report import TokenReadinessReport
from result import AnalysisResult
from util import LoggingLevelRouter


class KingReadinessAnalyzer(Analyzer):
    """
    Role:
        -   Analysis Factory
        -   Consistency maintenance


    Responsibilities:
        1.  ReadinessAnalyzerBootstrapper helper class which analyzes KingToken's
             availability.
        2.  Performs not safety checks on analysis subjet.

    Attributes:

    Provides:
        -   def execute(
                    subject: KingToken,
            ) -> AnalysisResult[TokenReadinessReport]
    Parent:
        Analyzer
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(cls, subject: KingToken,) -> AnalysisResult[TokenReadinessReport]:
        """
        Reports if a KingToken is free or not. Should not be called directly.
        Action:
            1.  Report the token is inactive if its checkmates or not deployed. Otherwise,
                report its free.
        Args:
            subject: KingToken
        Returns:
              AnalysisResult[TokenFreedomReport]
        Raises:
        Notes:
            -   Performs no integrity checks should not be called directly.
        """
        method = f"{cls.__name__}.analyze"
        
        if subject.is_checkmatedd or subject.is_not_deployed:
            return AnalysisResult.completed(TokenReadinessReport.inactive(subject))
        
        return AnalysisResult.completed(TokenReadinessReport.ready(subject))