# src/result/maneuver/state.py

"""
Module: result.maneuver.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import auto, Enum


class ManeuverState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),