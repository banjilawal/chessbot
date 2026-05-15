# src/analysis/relation/token/analyst.py

"""
Module: analysis.relation.token.analyst
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from util import LoggingLevelRouter, RelationReport
from system.relation import RelationAnalysis
from model.token import (
    TokenActivityState, TokenReadinessAnalysisException, CombatantToken,
    KingToken, Token, TokenValidation
)

class TokenReadinessAnalyzer(RelationAnalysis[TokenActivityState.FREE, Token]):
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
                    candidate_satellite: Token,
                    candidate_primary: TokenActivityState.FREE,
                    token_validator: TokenValidator,
            ) -> RelationReport[TokenActivityState, Token]
    Parent:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate_satellite: Token,
            candidate_primary: TokenActivityState.FREE = TokenActivityState.FREE,
            token_validator: TokenValidation = TokenValidation(),
    ) -> RelationReport[TokenActivityState, Token]:
        """
        MAke sure the token can be used.
        
        Action:
            1.  If the token fails its certification send an exception chain in the
                RelationReport.
            2.  Otherwise, decide if the token is actionable base on.
                    -   It hs it been deployed.
                    -   It has not been captured or, it has not been checkmated.
            3.  Send the success result.
        
        Args:
            candidate_satellite: Token
            candidate_primary: TokenActivityState
            token_validator: TokenValidator
        Returns:
              RelationReport[TokenActivityState, Token]
        Raises:
        
        """
        method = f"{cls.__name__}.analyze"
        
        # Handle the case that, the token does not pass a validation check.
        validation_result = token_validator.validate(rank=candidate_satellite)
        # Send the exception chain on failure.
        if validation_result.is_failure:
            return RelationReport.failure(
                TokenReadinessAnalysisException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenReadinessAnalysisException.MSG,
                    err_code=TokenReadinessAnalysisException.ERR_CODE,
                    mthd_rslt_type=TokenReadinessAnalysisException.MTHD_RSLT,
                    ex=validation_result.exception
                )
            )
        # Deal with the simplest universal case first, token has no been deployed.
        if candidate_satellite.is_not_deployed:
            return RelationReport.no_relation()
        
        if isinstance(candidate_satellite, CombatantToken):
            return cls._analyze_combatant_readiness(
                combatant=cast(CombatantToken, candidate_satellite)
            )
        return cls._analyze_king_readiness(king=cast(KingToken, candidate_satellite))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _analyze_combatant_readiness(
            cls,
            combatant: CombatantToken,
            aliveness_state = TokenActivityState.FREE,
    ) -> RelationReport[TokenActivityState, Token]:
        method = f"{cls.__name__}._analyze_combatant_readiness"
        
        # Captured tokens are not free.
        if combatant.has_entered_hostage_process:
            return RelationReport.bidirectional(
                primary=TokenActivityState.HOSTAGE_CREATED,
                satellite=combatant,
            )
        if combatant.recorded_as_hostage:
            return RelationReport.bidirectional(
                primary=TokenActivityState.HOSTAGE_IN_DATABASE,
                satellite=combatant,
            )
        if combatant.is_disabled:
            return RelationReport.bidirectional(
                primary=TokenActivityState.DEACTIVATED,
                satellite=combatant,
            )
        if combatant.is_active:
            return RelationReport.bidirectional(
                primary=TokenActivityState.FREE,
                satellite=combatant,
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _analyze_king_readiness(cls, king: KingToken) -> RelationReport[TokenActivityState, Token]:

        if king.is_in_check:
            return RelationReport.bidirectional(
                primary=TokenActivityState.IN_CHECK,
                satellite=king,
            )
        if king.is_checkmated:
            return RelationReport.bidirectional(
                primary=TokenActivityState.CHECKMATED,
                satellite=king,
            )
        if king.is_disabled:
            return RelationReport.bidirectional(
                primary=TokenActivityState.DEACTIVATED,
                satellite=king,
            )
        return RelationReport.bidirectional(
            primary=TokenActivityState.FREE,
            satellite=king,
        )