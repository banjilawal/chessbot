# src/report/move/analyzer/state.py

"""
Module: report.move.analyzer.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class RankElevationDecision(Enum):
    GRANTED = auto(),
    DENIED = auto(),