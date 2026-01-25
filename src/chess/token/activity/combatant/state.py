# src/chess/token/model/concrete/combatant/state.py

"""
Module: chess.token.model.concrete.combatant.state
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from enum import Enum, auto

class CombatantState(Enum):
    FREE = auto(),
    CAPTURE_ACTIVATED = auto(),
    ISSUED_HOSTAGE_MANIFEST = auto(),
    MANIFESTED_HOSTAGE_OFF_BOARD = auto(),
    