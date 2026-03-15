# src/logic/pair/stack/exception/push/wrapper.py

"""
Module: logic.pair.stack.exception.push.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# PUSHING_PAIR_FAILURE #======================#
    "PushingPairException",
]

from logic.pair import PairStackException
from logic.system import PushException


# ======================# PUSHING_PAIR_FAILURE #======================#
class PushingPairException(PairStackException, PushException):
    """
    # ROLE: Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why pushing a pair failed. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   PairException
        *   PushException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PUSHING_PAIR_FAILURE"
    MSG = "Pushing pair failed."