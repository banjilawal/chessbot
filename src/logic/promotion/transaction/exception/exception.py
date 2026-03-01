# src/logic/promotion/transaction/exception/exception.py

"""
Module: logic.promotion.transaction.exception.exception_
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from logic.system import TransactionException

__all__ = [
    "PromotionTransactionException",
]

class PromotionTransactionException(TransactionException):
    ERR_CODE = "PROMOTION_TRANSACTION_EXCEPTION"
    MSG = "PromotionTransaction raised an exception."