# src/logic/pair/stack/exception/query/exist.py

"""
Module: logic.pair.stack.exception.query.exist
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""



__all__ = [
    # ======================# PAIR_NOT_FOUND EXCEPTION #======================#
    "PairNotFoundException",
]

from logic.pair import PairDebugException


# ======================# PAIR_NOT_FOUND EXCEPTION #======================#
class PairNotFoundException(PairDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to remove instances of a item by a unique attribute failed because no bag
        matching the property were found in the collider_candidates.

    Super Class:
        *   NullException
        *   PairStackException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PAIR_NOT_FOUND_EXCEPTION"
    MSG = "Pair deletion failed: The item was not found in the collider_candidates. Nothing to remove."