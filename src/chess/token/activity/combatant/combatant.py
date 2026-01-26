# src/chess/occupant/state/activity/combatant/combatant.py

"""
Module: chess.occupant.state.activity.combatant.combatant
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from chess.token import ActivityState, CombatantReadinessEnum


class CombatantActivityState(ActivityState[CombatantReadinessEnum]):
    
    def __init__(self, classification: CombatantReadinessEnum):
        super().__init__(classification=classification)