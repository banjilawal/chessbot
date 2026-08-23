# src/artifact/result/analysis/state.py

"""
Module: artfifact.result.analysis.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import auto, Enum


class AnalysisState(Enum):
    ABORTED = auto(),
    COMPLETED = auto(),
    TIMED_OUT= auto(),