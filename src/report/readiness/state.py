# src/report/freedom/state.py

"""
Module: report.freedom.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class ReadinessState(Enum):
    READY = auto(),
    DISABLED = auto(),
    CAPTURED = auto(),
    CHECKMATED = auto(),
    NOT_DEPLOYED = auto(),
    