# src/result/computation/state.py

"""
Module: result.computation.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import auto, Enum


class ComputationState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),