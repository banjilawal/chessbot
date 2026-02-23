# src/chess/system/collection/operation/collision/exception/wrapper.py

"""
Module: chess.system.collection.operation.collision.exception.wrapper
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

from chess.system import OperationException

__all__ = [
    # ======================# COLLISION_DETECTION_FAILURE #======================#
    "CollisionDetectionException",
]


# ======================# COLLISION_DETECTION_FAILURE #======================#
class CollisionDetectionException(OperationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a collision detection operation failed. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COLLISION_DETECTION_FAILURE"
    DEFAULT_MESSAGE = "collision detection failed."