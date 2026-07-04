# src/analyzer/freedom/analyzer.py

"""
Module: analyzer.freedom.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analyzer import Analyzer
from bootstrap import ReadinessAnalyzerBootstrapper
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

    Provides:
        -   execute(
                    token: Token,
                    token_validator: TokenValidator,
            ) -> AnalysisResult[TokenFreedomReport]
            
    Parent:
        Analyzer
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            token: Token,
            bootstrapper: ReadinessAnalyzerBootstrapper | None = None,
    ) -> AnalysisResult[TokenReadinessReport]:
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
            bootstrapper: ReadinessAnalyzerBootstrapper
        Returns:
              AnalysisResult[TokenFreedomReport]
        Raises:
            TokenFreedomAnalyzerException
        """
        method = f"{cls.__name__}.analyze"
        
        # --- Supply any missing dependencies. ---#
        if bootstrapper is None:
            bootstrapper = ReadinessAnalyzerBootstrapper()
            
        analysis_result = bootstrapper.execute(token=token,)
        if analysis_result.is_failure:
            return AnalysisResult.failure(
                exception=TokenReadinessAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenReadinessAnalyzerException.MSG,
                    err_code=TokenReadinessAnalyzerException.ERR_CODE,
                    ex=analysis_result.exception
                )
            )
        return AnalysisResult.completed(TokenReadinessReport.ready(token=token))