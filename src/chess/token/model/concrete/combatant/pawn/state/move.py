# src/chess/token/model/concrete/combatant/pawn/state/move.py

"""
Module: chess.token.model.concrete.combatant.pawn.state.move
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto


class MoveCategory(Enum):
    NULL = auto(),
    OPENED = auto(),
    DEVELOPED = auto(),
