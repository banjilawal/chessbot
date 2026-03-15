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
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a item by a unique attribute failed because no bag
        matching the property were found in the dataset.

    # PARENT:
        *   NullException
        *   PairStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PAIR_NOT_FOUND_EXCEPTION"
    MSG = "Pair deletion failed: The item was not found in the dataset. Nothing to remove."