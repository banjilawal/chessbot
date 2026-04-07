# src/analysis/report/collision/state.py

"""
Module: analysis.report.collision.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class CollisionState(Enum):
    NO_COLLISIONS = auto(),
    COLLISION_DETECTED = auto(),