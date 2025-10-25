# src/chess/travel/promotion/transaction/exception.py

"""
Module: chess.travel.promotion.transaction.exception
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""

from chess.system import RollbackException
from chess.piece import OccupationTransactionException, TravelTransactionException

__all__ = [
    'PromotionTransactionException',
    'RolledBackPromotionTransactionException',
    'FailedPreviousRankUpdateRolledBackException' ,
    'FailedSetRankToQueenRolledBackException'
]

class PromotionTransactionException(TravelTransactionException):
    ERROR_CODE = "PROMOTION_TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "PromotionTransaction raised an exception."
    
class RolledBackPromotionTransactionException(PromotionTransactionException, RollbackException):
    ERROR_CODE = "PROMOTION_TRANSACTION_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Promotion transaction failed. Before raising this exception, the transaction was rolled back."
 
class FailedPreviousRankUpdateRolledBackException(RolledBackPromotionTransactionException):
 ERROR_CODE = "FAILED_UPDATING_PREVIOUS_RANK_ERROR_ROLLED_BACK"
 DEFAULT_MESSAGE = (
     "Updating the previous rank failed during a promotion transaction. The operation was rolled back "
     "before raising the exception."
 )
 
class FailedSetRankToQueenRolledBackException(RolledBackPromotionTransactionException):
    ERROR_CODE = "ROLLED_BACK_PROMOTION_TRANSACTION_ERROR"
    DEFAULT_MESSAGE = "Promotion transaction failed. The transaction was rolled back before raising the exception."