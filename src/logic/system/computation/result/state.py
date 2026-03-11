# src/logic/system/computation/state/__init__.py

"""
Module: logic.system.computation.state.__init__
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

from enum import auto, Enum


class ComputationState(Enum):
    """
    """
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),