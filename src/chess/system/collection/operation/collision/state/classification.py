# src/chess/system/collection/operation/collision/state/classification.py

"""
Module: chess.system.collection.operation.collision.state.classification
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

from enum import Enum, auto


class CollisionResultEnum(Enum):
    """
    """
    FAILURE = auto(),
    TIMED_OUT = auto(),
    NO_COLLISIONS = auto(),
    COLLISION_DETECTED = auto(),