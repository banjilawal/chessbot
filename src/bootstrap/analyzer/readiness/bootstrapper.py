# src/bootstrap/analyzer/readiness/bootstrapper.py

"""
Module: bootstrap.analyzer.readiness.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from bootstrap import AnalyzerBootstrapper
from err import ReadinessAnalyzerBootstrapperException
from model import CombatantToken, KingToken, Token
from report import TokenReadinessReport
from result import AnalysisResult
from util import LoggingLevelRouter
from validation import TokenValidator


class ReadinessAnalyzerBootstrapper(AnalyzerBootstrapper):
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
    def execute(
            cls,
            token: Token,
            token_validator: TokenValidator | None = None,
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
            token_validator: TokenValidator
        Returns:
              AnalysisResult[TokenFreedomReport]
        Raises:
            TokenFreedomAnalyzerException
        """
        method = f"{cls.__name__}.analyze"
        
        # --- Supply any missing dependencies. ---#
        if token_validator is None:
            token_validator = TokenValidator()
        
        # Handle the case that, the token does not pass a validation check.
        validation_result = token_validator.validate(token)
        # Send the exception chain on failure.
        if validation_result.is_failure:
            return AnalysisResult.failure(
                ReadinessAnalyzerBootstrapperException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ReadinessAnalyzerBootstrapperException.MSG,
                    err_code=ReadinessAnalyzerBootstrapperException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # Deal with the simplest universal case first, token has no been deployed.
        if token.is_not_deployed:
            return AnalysisResult.completed(TokenReadinessReport.inactive(token))
        
        if isinstance(token, CombatantToken):
            return cls._analyze_combatant_readiness(combatant=cast(CombatantToken, token))
        # Otherwise we are checking if a king is free.
        return cls._analyze_king_readiness(king=cast(KingToken, token))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _analyze_combatant_readiness(
            cls,
            combatant: CombatantToken,
    ) -> AnalysisResult[TokenReadinessReport]:
        # Captured tokens are not free.
        if combatant.has_entered_hostage_process or combatant.recorded_as_hostage:
            return AnalysisResult.completed(TokenReadinessReport.captured(combatant))
        # Disabled combatants are not free either.
        if combatant.is_disabled:
            return AnalysisResult.completed(TokenReadinessReport.disabled(combatant))
        
        return AnalysisResult.completed(TokenReadinessReport.ready(combatant))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _analyze_king_readiness(
            cls,
            king: KingToken
    ) -> AnalysisResult[TokenReadinessReport]:
        # Checkmated kings are not free.
        if king.is_checkmated:
            return AnalysisResult.completed(TokenReadinessReport.checkmated(king))
        # Disabled kings are not free either.
        if king.is_disabled:
            return AnalysisResult.completed(TokenReadinessReport.disabled(king))
        
        return AnalysisResult.completed(TokenReadinessReport.ready(king))