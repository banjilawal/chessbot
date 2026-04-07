# src/result/analysis/state.py

"""
Module: result.analysis.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import auto, Enum


class AnalysisState(Enum):
    ABORTED = auto(),
    COMPLETED = auto(),
    TIMED_OUT= auto(),