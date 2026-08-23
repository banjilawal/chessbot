# src/artifact/result/crud/insert/state.py

"""
Module: artfifact.result.insert.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import auto, Enum

class InsertionState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    ALREADY_INSERTED = auto(),