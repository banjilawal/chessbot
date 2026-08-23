# src/artifact/result/shell/interpretation/state.py

"""
Module: artfifact.result.shell.interpretation.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from enum import auto, Enum


class InterpretationState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    NOTHING_TO_INTERPRET = auto(),