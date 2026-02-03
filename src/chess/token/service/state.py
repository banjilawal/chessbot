from typing import cast

from chess.rank.model.concrete.king import King
from chess.system import ChessException, LoggingLevelRouter, RelationAnalyzer, RelationReport, ValidationResult
from chess.token import (
    ActivityState, CombatantToken, KingActivityState, KingReadinessEnum, KingToken, Token,
    TokenValidator
)


class TokenStateAnalysis(RelationAnalyzer[ActivityState, Token]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(cls, token, token_validator: TokenValidator) -> RelationReport[ActivityState, Token]:
        pass
        
        # validation = token_validator.validate(candidate=token)
        # if validation.is_failure:
        #     return ValidationResult.failure(validation.exception)
        #
        # if isinstance(token, KingToken):
        #     return cls._analyze_king_state(king=cast(KingToken, token))
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _analyze_combatant_state(cls, combatant: CombatantToken):
        if combatant.activity.classification ==
    


    @classmethod
    @LoggingLevelRouter.monitor
    def _analyze_king_state(cls, king: KingToken):
        if king.activity.classification == KingReadinessEnum.NOT_INITIALIZED:
            return RelationReport.bidirectional(
                primary=KingActivityState(KingReadinessEnum.NOT_INITIALIZED),
                satellite=king,
            )
        if king.is_in_check:
            return RelationReport.bidirectional(
                primary=KingActivityState(KingReadinessEnum.IN_CHECK),
                satellite=king,
            )
        if king.is_checkmated:
            return RelationReport.bidirectional(
                primary=KingActivityState(KingReadinessEnum.CHECKMATED),
                satellite=king,
            )
        if king.is_active:
            return RelationReport.bidirectional(
                primary=KingActivityState(KingReadinessEnum.CHECKMATED),
                satellite=king,
            )
        