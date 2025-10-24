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
            
            promoted_piece = cast()
            return TransactionResult.success(event_update=self.event)
        except Exception as e:
            return TransactionResult.errored(event_update=self.event, exception=e)
