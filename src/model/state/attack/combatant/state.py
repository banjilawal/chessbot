# src/model/state/attack/combatant/state.py

"""
Module: model.state.attack.combatant.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum, auto


class CombatantAttackState(Enum):
    ATTACK_COMPLETED = auto(),
    ATTACK_NOT_COMPLETED = auto(),