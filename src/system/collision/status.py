# src/logic/system/collision/state/classification.py

"""
Module: logic.system.collision.state.classification
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

from enum import Enum, auto


class CollisionStatus(Enum):
    """
    """
    NO_COLLISIONS = auto(),
    COLLISION_DETECTED = auto(),
    DETECTOR_FAILED = auto(),
    DETECTOR_TIMED_OUT = auto(),