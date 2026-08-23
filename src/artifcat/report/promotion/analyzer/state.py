# src/artifact/report/promotion/analyzer/state.py

"""
Module: artfifact.report.promotion.analyzer.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import Enum, auto


class RankElevationDecision(Enum):
    GRANTED = auto(),
    DENIED = auto(),