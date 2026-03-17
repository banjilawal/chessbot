# src/logic/system/collision/exception/unsupported.py

"""
Module: logic.system.collision.exception.unsupported
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

__all__ = [
    # ======================# UNSUPPORTED_EMPTY_COLLISION_RESULT_STATE EXCEPTION #======================#
    "UnsupportedEmptyCollisionResultException",
]

from logic.system import UnsupportedDataResultStateException


# ======================# UNSUPPORTED_EMPTY_COLLISION_RESULT_STATE EXCEPTION #======================#
class UnsupportedEmptyCollisionResultException(UnsupportedDataResultStateException):
    """
    Role:Information, Reporting, Debug

    Responsibilities:
    1.  Indicate that an CollisionReport can either succeed or fail. There are no other outcomes.

    Super Class:
        *   UnsupportedDataResultStateException

    Provides:


    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "UNSUPPORTED_EMPTY_COLLISION_RESULT_STATE_EXCEPTION"
    MSG = (
        "An CollisionReport's outcome is either changed, change_failed, collision original == collision, failure."
        " It cannot be empty."
    )