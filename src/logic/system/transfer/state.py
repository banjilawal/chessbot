# src/logic/system/transfer/state.py

"""
Module: logic.system.transfer.state
Author: Banji Lawal
Created: 2026-02-01
version: 1.0.0
"""

from enum import Enum, auto


class TransferResultState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    ROLLED_BACK = auto(),
    ROLLED_BACK_TIMEOUT = auto(),
