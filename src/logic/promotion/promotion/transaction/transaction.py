# src/logic/travel/promotion/transaction/transaction.py

"""
Module: logic.travel.promotion.transaction.transaction
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""


from logic.rank import Queen
from logic.system import LoggingLevelRouter, TransactionResult
from logic.piece import (
    TravelTransaction, PromotionEvent, PromotionEventValidator, FailedPreviousRankUpdateRolledBackException,
    FailedSetRankToQueenRolledBackException
)


class OldPromotionTransaction(TravelTransaction[PromotionEvent]):
    """"""
    def __init__(self, event: PromotionEvent):
        super().__init__(event)
    
    @LoggingLevelRouter.monitor
    def execute(self) -> TransactionResult:
        """"""
        method = "PromotionTransaction.execute"
        
        try:
            event_validation = PromotionEventValidator.validate(self.event)
            if event_validation.failure():
                return TransactionResult.errored(event_update=self.event, exception=event_validation.exception)
            
            self.event.actor.previous_rank = self.event.actor.rank_name
            if self.event.actor.previous_rank is None:
                return TransactionResult.rolled_back(
                    event_update=self.event,
                    rollback_exception=FailedPreviousRankUpdateRolledBackException(
                        f"{method}: {FailedPreviousRankUpdateRolledBackException.MSG}"
                    )
                )
        
            self.event.actor.set_new_rank(self.event.new_rank)
            if not isinstance(self.event.actor.rank_name, self.event.new_rank):
                self.event.actor._set_rank(self.event.actor.previous_rank)
                self.event.actor.previous_rank = None
                
                return TransactionResult.rolled_back(
                    event_update=self.event,
                    rollback_exception=FailedSetRankToQueenRolledBackException(
                        f"{method}: {FailedSetRankToQueenRolledBackException.MSG}"
                    )
                )
            
            return TransactionResult.success(event_update=self.event)
        except Exception as e:
            return TransactionResult.errored(event_update=self.event, exception=e)


