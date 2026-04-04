# src/logic/pair/schema/exception/deletion/empty.py

"""
Module: logic.pair.schema.exception.deletion.empty
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from graph.pair import PairStackException


__all__ = [
    # ======================# POPPING_EMPTY_PAIR_STACK EXCEPTION #======================#
    "PoppingEmptyPairStackException",
]

# ======================# POPPING_EMPTY_PAIR_STACK EXCEPTION #======================#
class PoppingEmptyPairStackException(PairStackException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to remove a occupant failed because the PairStack was not managing any pairs.

    Super Class:
        *   TeamDaaServiceException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_EMPTY_PAIR_STACK_EXCEPTION"
    MSG = "Pair deletion failed: PairStack does not own any pairs."