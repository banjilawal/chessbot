# src/domain/model/searchable/state/attack/king/state.py

"""
Module: domain.model.searchable.state.walk.attack.king.state
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class KingAttackState(Enum):
    CHECKED_ENEMY_KING = auto(),
    ATTACK_NOT_COMPLETED = auto(),