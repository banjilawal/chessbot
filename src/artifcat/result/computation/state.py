# src/artifact/result/computation/state.py

"""
Module: artfifact.result.computation.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import auto, Enum


class ComputationState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),