# src/report/claim/state.py

"""
Module: report.claim.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class claimState(Enum):
    FREE = auto(),
    DISABLED = auto(),
    CAPTURED = auto(),
    CHECKMATED = auto(),
    NOT_DEPLOYED = auto(),