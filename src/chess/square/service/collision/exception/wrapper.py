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

from chess.system import CollisionDetectionException


# ======================# COLLISION_DETECTION_OPERATION_FAILURE #======================#
class SquareCollisionDetectionException(CollisionDetectionException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in SquareCollisionDetector.detect that prevented a successful, no collisions
        detected result.

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
    DEFAULT_MESSAGE = "SquareCollisionDetection operation failed."