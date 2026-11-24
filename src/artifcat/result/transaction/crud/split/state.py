# src/artifact/result/transaction/crud/split/state.py

"""
Module: artfifact.result.transaction.crud.split.state.
Created: 2026-04-03
version: 0.0.2
"""

from enum import auto, Enum

class SplitState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    NOTHING_TO_DELETE = auto(),