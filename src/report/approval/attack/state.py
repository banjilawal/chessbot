# src/report/approval/attack/state.py

"""
Module: report.approval.attack.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class AttackPermission(Enum):
    KING_ATTACK_GRANTED = auto(),
    COMBATANT_ATTACK_GRANTED = auto(),
    DENIED = auto()