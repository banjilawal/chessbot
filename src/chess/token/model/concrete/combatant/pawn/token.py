# src/chess/token/model/concrete/combatant/pawn/occupant.py

"""
Module: chess.token.model.concrete.combatant.pawn.occupant
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from chess.team import Team
from chess.rank import Pawn, Rank
from chess.token import CombatantToken, MoveCategory, PromotionState


class PawnToken(CombatantToken):
    _promotion_state: PromotionState
    
    def __init__(
            self,
            id: int,
            team: Team,
            designation: str,
            roster_number: int,
            opening_square_name: str,
    ):
        super().__init__(
            id=id,
            team=team,
            rank=Pawn(),
            designation=designation,
            roster_number=roster_number,
            opening_square_name=opening_square_name
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
    def promotion_state(self, promotion_state: PromotionState):
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
    
    def set_new_rank(self, new_rank: Rank):
        self._set_rank(new_rank)
       
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, PawnToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
