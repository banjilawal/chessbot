# src/report/collision/state.py

"""
Module: report.collision.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class ClaimPermission(Enum):
    GRANTED = auto(),
    DENIED = auto(),