# src/analyzer/readiness/combatant/analyzer.py

"""
Module: analyzer.readiness.combatant.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analyzer import Analyzer
from model import CombatantToken
from report import TokenReadinessReport
from result import AnalysisResult
from util import LoggingLevelRouter


class CombatantReadinessAnalyzer(Analyzer):
    """
    Role:
        -   Analysis Factory
        -   Consistency maintenance


    Responsibilities:
        1.  ReadinessAnalyzerBootstrapper helper class which analyzes CombatantToken's
             availability.
        2.  Performs not safety checks on analysis subjet.

    Attributes:

    Provides:
        -   def execute(
                    subject: CombatantToken,
            ) -> AnalysisResult[TokenReadinessReport]
    Parent:
        Analyzer
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, subject: CombatantToken, ) -> AnalysisResult[TokenReadinessReport]:
        """
        Reports if a CombatantToken is free or not. Should not be called directly.
        Action:
            1.  Report the token is inactive if its captured or not deployed. Otherwise,
                report its free.
        Args:
            subject: CombatantToken
        Returns:
              AnalysisResult[TokenFreedomReport]
        Raises:
        Notes:
            -   Performs no integrity checks should not be called directly.
        """
        method = f"{cls.__name__}.analyze"
        
        if subject.is_captured or subject.is_not_deployed:
            return AnalysisResult.completed(TokenReadinessReport.inactive(subject))
        
        return AnalysisResult.completed(TokenReadinessReport.ready(subject))