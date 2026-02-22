# src/chess/square/square/service/collision/wrapper.py

"""
Module: chess.square.service.collision.wrapper
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# COLLISION_DETECTION_OPERATION_FAILURE #======================#
    "SquareCollisionDetectionException",
]




# ======================# COLLISION_DETECTION_OPERATION_FAILURE #======================#
class SquareCollisionDetectionException(CollisionDetectionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why square collision detection operation failed. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   CollisionDetectionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COLLISION_DETECTION_OPERATION_FAILURE"
    DEFAULT_MESSAGE = "Square collision detection operation failed."