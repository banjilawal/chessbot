# src/chess/token/combatant/pawn/token.py

"""
Module: chess.token.combatant.pawn.token
Author: Banji Lawal
Created: 2025-11-23
version: 1.0.0
"""

from typing import Optional

from chess.rank import Pawn, Rank
from chess.square import Square
from chess.team import Team
from chess.token import CombatantToken, PromotionState


class PawnToken(CombatantToken):
    _previous_rank: Optional[Rank]
    _promotion_state: PromotionState
    
    def __init__(
            self,
            id: int,
            rank: Rank,
            team: Team,
            designation: str,
            roster_number: int,
            opening_square: Square,
    ):
        super().__init__(
            id=id,
            team=team,
            rank=rank,
            designation=designation,
            roster_number=roster_number,
            opening_square=opening_square
        )
        self._previous_rank = None
        self._promotion_state = PromotionState.NOT_PROMOTED
    
    @property
    def previous_rank(self) -> Optional[Rank]:
        return self._previous_rank
    
    @property
    def promotion_state(self) -> PromotionState:
        return self._promotion_state
    
    @promotion_state.setter
    def promotion(self, promotion_state: PromotionState):
        self._promotion_state = promotion_state
        
    @property
    def can_promote(self) -> bool:
        return (
            self.is_active and not self.is_promoted and
            self.current_position.row == self.team.schema.opposite.pawn_row
        )
    
    @property
    def is_promoted(self) -> bool:
        return not isinstance(self.rank, Pawn) and self._promotion_state != PromotionState.NOT_PROMOTED
    
    def promote(self, new_rank: Rank):
        self._set_rank(new_rank)
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, PawnToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
