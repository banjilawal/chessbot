# src/artifact/result/attack/state.py

"""
Module: artfifact.result.attack.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto

class AttackState(Enum):
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    CHECKMATE = auto(),
    COMBATANT_KILLED = auto(),
    CHECK_WARNING_ISSUED = auto(),
    