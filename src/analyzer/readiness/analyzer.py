# src/analyzer/freedom/analyzer.py

"""
Module: analyzer.freedom.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analyzer import Analyzer
from bootstrapper import ReadinessAnalyzerBootstrapper
from err import TokenReadinessAnalyzerException
from model import Token
from report import TokenReadinessReport
from result import AnalysisResult
from util import LoggingLevelRouter


class TokenReadinessAnalyzer(Analyzer):
    """
    Role:
        -   Analysis Factory
        -   Consistency maintenance
        
    Responsibilities:
        1.  Analyze a token's aliveness before its used in the brought into play.
        2.  Combine safety and aliveness tests unique to each subclass under one roof.

    Attributes:
        carrier_validator: ReadinessAnalyzerBootstrapper
        
    Provides:
        -   execute(token: Token,) -> AnalysisResult
            
    Parent:
        Analyzer
    """
    _bootstrapper: ReadinessAnalyzerBootstrapper
    
    def __init__(
            self,
            bootstrapper: ReadinessAnalyzerBootstrapper | None = ReadinessAnalyzerBootstrapper(),
    ):
        """
        Args:
            bootstrapper: ReadinessAnalyzerBootstrapper
        """
        self._bootstrapper = bootstrapper
    
    
    @LoggingLevelRouter.monitor
    def execute(self, token: Token) -> AnalysisResult[TokenReadinessReport]:
        """
        MAke sure the token can be used.
        
        Action:
            1.  If the token fails, its certification, send an exception chain in the
                RelationReport.
            2.  Otherwise, decide if the token is actionable based on.
                    -   if it has been deployed.
                    -   It has not been captured or checkmated.
            3.  Send the success result.
        
        Args:
            token: Token
            carrier_validator: ReadinessAnalyzerBootstrapper
        Returns:
              AnalysisResult[TokenFreedomReport]
        Raises:
            TokenFreedomAnalyzerException
        """
        method = f"{self.__class__.__name__}.analyze"
        
        # --- Supply any missing dependencies. ---#
            
        analysis_result = self._bootstrapper.execute(subject=token, )
        if analysis_result.is_failure:
            return AnalysisResult.failure(
                exception=TokenReadinessAnalyzerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenReadinessAnalyzerException.MSG,
                    err_code=TokenReadinessAnalyzerException.ERR_CODE,
                    ex=analysis_result.exception
                )
            )
        return AnalysisResult.completed(TokenReadinessReport.ready(token=token))