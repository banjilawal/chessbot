# src/logic/pair/schema/exception/deletion/validator.py

"""
Module: logic.pair.schema.exception.deletion.work
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# POPPING_PAIR_FAILURE #======================#
    "PoppingPairException",
]

from logic.system import DeletionException
from logic.pair import PairException


# ======================# POPPING_PAIR_FAILURE #======================#
class PoppingPairException(PairException, DeletionException):
    """
    Role:Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    Responsibilities:
    1.  Wrap debug exceptions indicating why popping a pair failed. The exception chain
        traces the ultimate source of failure.

    Super Class:
        *   PairException
        *   DeletionException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_PAIR_FAILURE"
    MSG = "Popping pair failed."