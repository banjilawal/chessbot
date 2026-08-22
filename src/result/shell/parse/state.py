# src/result/shell/delete/state.py

"""
Module: result.delete.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import auto, Enum


class ParseState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),