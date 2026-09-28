# src/artifact/result/crud/update/state.py

"""
Module: artfifact.result.crud.update.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto

class UpdateState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    NOTHING_TO_UPDATE = auto(),
    CALLED_UNIMPLEMENTED_METHOD = auto(),