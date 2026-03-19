# src/logic/token/service/operation/analysis.py

"""
Module: logic.token.service.operation.analysis
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

import token
from typing import cast

from logic.system import LoggingLevelRouter, RelationReport
from logic.system.relation.analysis import RelationAnalysis
from logic.token import (
    ReadinessStateNullException, TokenException, ReadinessState, TokenReadinessAnalysisException, CombatantToken,
    KingToken, Token, TokenValidation
)

class TokenReadinessAnalysis(RelationAnalysis[ReadinessState.FREE, Token]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate_satellite: Token,
            candidate_primary: ReadinessState = ReadinessState.FREE,
            token_validator: TokenValidation = TokenValidation(),
    ) -> RelationReport[ReadinessState, Token]:
        """
        Analyses if a Token is ready
        
        Args:
            candidate_satellite: Token
            candidate_primary: ReadinessState
            token_validator: TokenValidator
        Returns:
              RelationReport[ReadinessState, Token]
        Raises:
        
        """
        method = f"{cls.__name__}.analyze"
        
        # Handle the case that, the candidate_secondary does not exist.
        if candidate_primary is None:
            candidate_primary = ReadinessState.FREE
        
        # Handle the case that, the token is not certified as safe.
        validation_result = token_validator.execute(candidate=candidate_satellite)
        # Send the exception chain on failure.
        if validation_result.is_failure:
            return RelationReport.failure(
                TokenReadinessAnalysisException(
                    mthd=method,
                    title=cls.__name__,
                    msg=TokenReadinessAnalysisException.MSG,
                    err_code=TokenReadinessAnalysisException.ERR_CODE,
                    rslt_type=TokenReadinessAnalysisException.RSLT_TYPE,
                    ex=validation_result.exception
                )
            )
        
        if candidate_satellite.is_not_deployed:
            return
            
        if isinstance(candidate_satellite, CombatantToken):
            return cls._analyze_combatant_readiness(combatant=cast(CombatantToken, candidate_satellite))
        return cls._analyze_king_readiness(king=cast(KingToken, candidate_satellite))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _analyze_combatant_readiness(cls, combatant: CombatantToken) -> RelationReport[ReadinessState, Token]:
        if combatant.has_entered_hostage_process:
            return RelationReport.bidirectional(
                primary=ReadinessState.HOSTAGE_CREATED,
                satellite=combatant,
            )
        if combatant.recorded_as_hostage:
            return RelationReport.bidirectional(
                primary=ReadinessState.HOSTAGE_IN_DATABASE,
                satellite=combatant,
            )
        if combatant.is_disabled:
            return RelationReport.bidirectional(
                primary=ReadinessState.DEACTIVATED,
                satellite=combatant,
            )
        if combatant.is_active:
            return RelationReport.bidirectional(
                primary=ReadinessState.FREE,
                satellite=combatant,
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _analyze_king_readiness(cls, king: KingToken) -> RelationReport[ReadinessState, Token]:

        if king.is_in_check:
            return RelationReport.bidirectional(
                primary=ReadinessState.IN_CHECK,
                satellite=king,
            )
        if king.is_checkmated:
            return RelationReport.bidirectional(
                primary=ReadinessState.CHECKMATED,
                satellite=king,
            )
        if king.is_disabled:
            return RelationReport.bidirectional(
                primary=ReadinessState.DEACTIVATED,
                satellite=king,
            )
        return RelationReport.bidirectional(
            primary=ReadinessState.FREE,
            satellite=king,
        )