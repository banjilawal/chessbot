from chess.piece import PromotionEventValidator, TravelEvent, TravelTransaction
from chess.piece.travel.promotion.event import PromotionEvent
from chess.system import LoggingLevelRouter, TransactionResult


class PromotionTransaction(TravelTransaction[PromotionEvent]):
    
    def __init__(self, event: TravelEvent):
        super().__init__(event)
    
    @LoggingLevelRouter.monitor
    def execute(self) -> TransactionResult:
        """"""
        method = "PromotionTransaction.execute"
        
        try:
            event_validation = PromotionEventValidator.validate(self.event)
            if event_validation.failure():
                return TransactionResult.errored(event_update=self.event, exception=event_validation.exception)
            
           self.event.actor.promote()
           if not isinstance(self.event.actor.rank, Queen):
               return TransactionResult.roll_back(
                   event_update=self.event,
                   exception=FailedPromotionRolledBackException(f"{method}: Failed to promote {event.actor.rank} to Queen.")
               )
            
            return TransactionResult.success(event_update=self.event)
        except Exception as e:
            return TransactionResult.errored(event_update=self.event, exception=e)

