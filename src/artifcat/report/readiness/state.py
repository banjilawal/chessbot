# src/artifact/report/freedom/state.py

"""
Module: artfifact.report.freedom.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import Enum, auto


class ReadinessState(Enum):
    READY = auto(),
    DISABLED = auto(),
    CAPTURED = auto(),
    CHECKMATED = auto(),
    NOT_DEPLOYED = auto(),
    