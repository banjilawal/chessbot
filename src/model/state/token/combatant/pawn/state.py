# src/model/state/token/model/state/concrete/combatant/pawn_token/state.py

"""
Module: model.state.token.model.concrete.combatant.pawn_token.state
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto

class PromotionState(Enum):
    PROMOTED = auto(),
    NOT_PROMOTED = auto(),
