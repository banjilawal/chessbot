# src/chess/system/collection/operation/collision/exception/wrapper.py

"""
Module: chess.system.collection.operation.collision.exception.wrapper
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

from chess.system import CollectionOperationException

__all__ = [
    # ======================# COLLISION_DETECTION_FAILURE #======================#
    "CollisionDetectionException",
]


# ======================# COLLISION_DETECTION_FAILURE #======================#
class CollisionDetectionException(CollectionOperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes why the collision detection operation was aborted.

    # PARENT:
        *   CollectionOperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COLLISION_DETECTION_FAILURE"
    DEFAULT_MESSAGE = "Collision detection failed."