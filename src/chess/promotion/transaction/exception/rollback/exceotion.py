# src/chess/promotion/transaction/exception/rollback/exception.py

"""
Module: chess.promotion.transaction.exception.rollback.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""


from chess.system import RollbackException
from chess.promotion.promotion import PromotionTransactionException

class PromotionTransactionRolledBackException(
    PromotionTransactionException,
    RollbackException
):
    ERR_CODE = "PROMOTION_TRANSACTION_ROLLED_BACK_ERROR"
    MSG = (
        "PromotionTransaction failed. The transaction was rolled back before "
        "this exception was raised."
    )