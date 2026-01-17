# src/chess/token/model/combatant/pawn/state.py

"""
Module: chess.token.model.combatant.pawn.state
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto

class PromotionState(Enum):
    NO_PROMOTION = auto(),
    PROMOTED_TO_QUEEN = auto(),
    PROMOTED_TO_CASTLE = auto(),