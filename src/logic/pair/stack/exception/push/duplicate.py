# src/logic/pair/database/exception/push/duplicate.py

"""
Module: logic.pair.database.exception.push.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from logic.pair import PairStackException

__all__ = [
    # ======================# ADDING_DUPLICATE_PAIR EXCEPTION #======================#
    "AddingDuplicatePairException",
]


# ======================# ADDING_DUPLICATE_PAIR EXCEPTION #======================#
class AddingDuplicatePairException(PairStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that pushing a pair onto the stack failed because it was already present in the stack.

    # PARENT:
        *   PairStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ADDING_DUPLICATE_PAIR_EXCEPTION"
    MSG = "Pushing pair failed: The pair was already present in the stack."