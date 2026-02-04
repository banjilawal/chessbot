# src/chess/token/state/analyzer.py

"""
Module: chess.token.state.analyzer
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.token import (
    NullTokenStateException, Token, TokenException, ReadinessState, TokenService, TokenState,
    TokenStateAnalysisFailedException
)
from chess.system import RelationAnalyzer, RelationReport


class TokenStateAnalyzer(RelationAnalyzer[TokenState, Token]):
    
    @classmethod
    def analyze(
            cls,
            candidate_satellite: Token,
            candidate_primary: TokenState,
            token_service: TokenService = TokenService(),
    ) -> RelationReport[TokenState, Token]:
        """"""
        method = "TokenStateAnalyzer.analyze"

        # Handle the case that the candidate_satellites is not certified.
        token_validation = token_service.validator.validate(candidate=candidate_satellite)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                TokenStateAnalysisFailedException(
                    message=f"{method}: {TokenStateAnalysisFailedException.DEFAULT_MESSAGE}",
                    ex=token_validation.exception
                )
            )


from __future__ import annotations
from typing import cast

from chess.rank.model.concrete.king import King
from chess.system import ChessException, LoggingLevelRouter, RelationAnalyzer, RelationReport, ValidationResult
from chess.token import (
    ActivityState, CombatantToken, KingActivityState, KingReadinessEnum, KingToken, Token,
    TokenValidator
)


class TokenReadinessAnalysis(RelationAnalyzer[ActivityState, Token]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            candidate_satellite: Token,
            token_validator: TokenValidator = TokenValidator(),
            candidate_primary: ReadinessState = ReadinessState(),
    ) -> RelationReport[ReadinessState, Token]:
        method = "TokenReadinessAnalysis.analyze"
        
        # Handle the case that the candidate_primary does not exist.
        if candidate_primary is None:
            # Return the exception chain on failure.
            return RelationReport.failure(
                TokenStateAnalysisFailedException(
                    message=f"{method}: {TokenStateAnalysisFailedException.DEFAULT_MESSAGE}",
                    ex=NullTokenStateException(f"{method}: {TokenStateAnalysisFailedException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the candidate_primary is the wrong type.
        if not isinstance(candidate_primary, TokenState):
            # Return the exception chain on failure.
            return RelationReport.failure(
                TokenStateAnalysisFailedException(
                    message=f"{method}: {TokenStateAnalysisFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected TokenState, got {type(candidate_primary).__name__} instead.")
                )
            )
        
        # Handle the case that the token is not certified as safe.
        validation_result = token_validator.validate(candidate=candidate_satellite)
        # Send the exception chain on failre.
        if validation_result.is_failure:
            return RelationReport.failure(
                TokenException(
                    f"{method}: {TokenException.DEFAULT_MESSAGE}",
                    ex=validation_result.exception
                )
            )
        if isinstance(candidate_satellite, CombatantToken):
            return cls._analyze_combatant_readiness(combatant=cast(CombatantToken, candidate_satellite))
        return cls._analyze_king_readiness(king=cast(KingToken, candidate_satellite))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _analyze_combatant_readiness(cls, combatant: CombatantToken) -> RelationReport[ReadinessState, Token]:
        if combatant.capture_is_activated:
            return RelationReport.bidirectional(
                primary=ReadinessState.HOSTAGE_MANIFEST_CREATED,
                satellite=combatant,
            )
        if combatant.capture_is_in_database:
            return RelationReport.bidirectional(
                primary=ReadinessState.HOSTAGE_MANIFEST_IN_DATABASE,
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