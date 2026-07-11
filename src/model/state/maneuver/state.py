# src/model/state/maneuver/state.py

"""
Module: model.state.maneuver.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum, auto


class ManeuverState(Enum):
    COMPLETED = auto(),
    NOT_COMPLETED = auto(),