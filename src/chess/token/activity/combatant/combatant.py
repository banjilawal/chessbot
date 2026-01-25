# src/chess/token/state/activity/combatant/combatant.py

"""
Module: chess.token.state.activity.combatant.combatant
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from abc import ABC
from enum import Enum

from chess.token import ActivityState
from chess.token.activity.combatant.state import CombatantState


class CombatantActivityState(ActivityState, ABC):
    _state: Enum
    
    def __init__(self, state: CombatantState):
        super().__init__(state=state)