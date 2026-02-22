# src/chess/token/database/core/util/detector/wrapper.py

"""
Module: chess.token.service.detector.wrapper
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# COLLISION_DETECTION_OPERATION_FAILURE #======================#
    "TokenCollisionDetectionException",
]




# ======================# COLLISION_DETECTION_OPERATION_FAILURE #======================#
class TokenCollisionDetectionException(CollisionDetectionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why token collision detection operation failed. The exception chain
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
    DEFAULT_MESSAGE = "Token collision detection operation failed."