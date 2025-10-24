from chess.piece import TravelTransactionException
from chess.system import RollbackException

__all__ = [
    'PromotionTransactionException',
    'RolledBackPromotionTransactionException'
]

class PromotionTransactionException(TravelTransactionException):
    ERROR_CODE = "PROMOTION_TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "Exception raised during PromotionTransaction."
    
class RolledBackPromotionTransactionException(PromotionTransactionException, RollbackException):
    ERROR_CODE = "ROLLED_BACK_PROMOTION_TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "Promotion transaction failed. The transaction was rolled back before raising the exception."
    