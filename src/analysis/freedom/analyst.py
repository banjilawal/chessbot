# src/analysis/freedom/analyst.py

"""
Module: analysis.freedom.analyst
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analysis import Analyst
from err import TokenFreedomAnalysisException
from model import CombatantToken, KingToken, Token
from report import TokenFreedomReport
from result import AnalysisResult
from util import LoggingLevelRouter
from validation import TokenValidator


class TokenFreedomAnalyzer(Analyst[Token]):
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
        Analyst
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            token_validator: TokenValidator | None = None,
    ) -> AnalysisResult[TokenFreedomReport]:
        """
        MAke sure the token can be used.
        
        Action:
            1.  If the token fails its certification send an exception chain in the
                RelationReport.
            2.  Otherwise, decide if the token is actionable base on.
                    -   It has it been deployed.
                    -   It has not been captured or, it has not been checkmated.
            3.  Send the success result.
        
        Args:
            token: Token
            token_validator: TokenValidator
        Returns:
              AnalysisResult[TokenFreedomReport]
        Raises:
            TokenFreedomAnalysisException
        """
        method = f"{cls.__name__}.analyze"
        
        
        if token_validator is None:
            token_validator = TokenValidator()
        
        # Handle the case that, the token does not pass a validation check.
        validation_result = token_validator.validate(candidate=token)
        # Send the exception chain on failure.
        if validation_result.is_failure:
            return AnalysisResult.failure(
                TokenFreedomAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenFreedomAnalysisException.MSG,
                    err_code=TokenFreedomAnalysisException.ERR_CODE,
                    mthd_rslt_type=TokenFreedomAnalysisException.MTHD_RSLT,
                    ex=validation_result.exception
                )
            )
        # Deal with the simplest universal case first, token has no been deployed.
        if token.is_not_deployed:
            return AnalysisResult.success(TokenFreedomReport.not_deployed(token))
        
        if isinstance(token, CombatantToken):
            return cls._analyze_combatant_freedom(
                combatant=cast(CombatantToken, token)
            )
        return cls._analyze_king_freedom(king=cast(KingToken, token))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _analyze_combatant_freedom(cls, combatant: CombatantToken,) -> AnalysisResult[TokenFreedomReport]:
        # Captured tokens are not free.
        if combatant.has_entered_hostage_process or combatant.recorded_as_hostage:
            return AnalysisResult.success(TokenFreedomReport.captured(combatant))
        if combatant.is_disabled:
            return AnalysisResult.success(TokenFreedomReport.disabled(combatant))
        
        return AnalysisResult.success(TokenFreedomReport.free(combatant))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _analyze_king_freedom(cls, king: KingToken) -> AnalysisResult[TokenFreedomReport]:

        if king.is_in_check:
            return AnalysisResult.success(TokenFreedomReport.checkmated(king))
        if king.is_disabled:
            return AnalysisResult.success(TokenFreedomReport.disabled(king))
        
        return AnalysisResult.success(TokenFreedomReport.free(king))