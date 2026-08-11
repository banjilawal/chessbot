# src/result/update/state.py

"""
Module: result.update.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class UpdateState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    NOTHING_TO_UPDATE = auto(),
    CALLED_UNIMPLEMENTED_METHOD = auto(),