# src/chess/token/model/concrete/combatant/pawn/state/promotion.py

"""
Module: chess.token.model.concrete.combatant.pawn.state.promotion
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto

class PromotionState(Enum):
    NOT_PROMOTED = auto(),
    PROMOTED_TO_QUEEN = auto(),
    PROMOTED_TO_CASTLE = auto(),
    PROMOTED_TO_BISHOP = auto(),
    PROMOTED_TO_KNIGHT = auto(),
