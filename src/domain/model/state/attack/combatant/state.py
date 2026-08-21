# src/dossier/model/state/attack/combatant/state.py

"""
Module: domain.model.state.attack.combatant.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class CombatantAttackState(Enum):
    ATTACK_COMPLETED = auto(),
    ATTACK_NOT_COMPLETED = auto(),