# src/logic/travel/promotion/transaction/collision.py

"""
Module: logic.travel.promotion.transaction.exception
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""

from logic.system import RollbackException
from logic.piece import OccupationTransactionException, TravelTransactionException

__all__ = [
    'PromotionTransactionException',
    'RolledBackPromotionTransactionException',
    'FailedPreviousRankUpdateRolledBackException' ,
    'FailedSetRankToQueenRolledBackException'
]

class PromotionTransactionException(TravelTransactionException):
    ERR_CODE = "PROMOTION_TRANSACTION_EXCEPTION"
    MSG = "PromotionTransaction raised an exception."
    
class RolledBackPromotionTransactionException(PromotionTransactionException, RollbackException):
    ERR_CODE = "PROMOTION_TRANSACTION_EXCEPTION_ROLLED_BACK"
    MSG = "Promotion transaction failed. Before raising this exception, the transaction was rolled back."
 
class FailedPreviousRankUpdateRolledBackException(RolledBackPromotionTransactionException):
 ERR_CODE = "FAILED_UPDATING_PREVIOUS_RANK_EXCEPTION_ROLLED_BACK"
 MSG = (
     "Updating the original bounds failed during a promotion transaction. The operation was rolled back "
     "before raising the exception."
 )
 
class FailedSetRankToQueenRolledBackException(RolledBackPromotionTransactionException):
    ERR_CODE = "ROLLED_BACK_PROMOTION_TRANSACTION_EXCEPTION"
    MSG = "Promotion transaction failed. The transaction was rolled back before raising the exception."