# src/artifact/result/state.py

"""
Module: artfifact.result.state
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class ResultState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),