# src/artifact/report/decision/state/_state.py

"""
Module: artfifact.report.decision.state._state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import Enum, auto


class Permission(Enum):
    GRANTED = auto(),
    DENIED = auto(),