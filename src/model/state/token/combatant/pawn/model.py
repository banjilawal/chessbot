# src/model/state/token/combatant/pawn/model/state.py

"""
Module: model.state.token.combatant.pawn.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import Formation, HomeSquare
from model.state.team import Team
from model.rank import Pawn, Rank
from model.state.token import CombatantToken, PromotionState


class PawnToken(CombatantToken):
    """
    Role:
        -   Stateful Data Holder

    Responsibilities:
        1.  Promotable combatant.

    Attributes:
        id: int
        team: Team
        rank: Rank
        designation: str
        roster_number: int
        positions: CoordDatabase
        home_square: OpeningSquare
        current_position: Optional[Coord]
        previous_address: Optional[Coord]
        token_board_state: TokenBoardState
        readiness_state: TokenActivityState
        is_not_deployed: bool
        is_active(self): bool
        is_disabled: bool
        is_enemy: bool
        has_entered_hostage_process: bool
        being_processed_as_hostage: bool
        recorded_as_hostage: bool
        captor: Optional[Token]
        previous_rank: Optional[Rank]
        promotion_state:
        previous_rank: Optional[Rank]
        can_promote:  bool
        is_promoted: bool
        
    Provides:
        -   set_new_rank(new_rank: Rank):
        
    Super Class:
        CombatantToken
    """
    _promotion_state: PromotionState
    
    def __init__(
            self,
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
    ):
        """
        Args:
            id: int
            team: Team
            rank: Rank
            designation: str
            roster_number: int
            home_square: OpeningSquare
        """
        super().__init__(
            id=id,
            team=team,
            rank=Pawn(formation.persona),
            formation=formation,
            home_square=home_square,
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
            self.current_position.row == self.team.schema.enemy_schema.pawn_row
        )
    
    @property
    def is_promoted(self) -> bool:
        return not isinstance(self.rank, Pawn) and self._promotion_state != PromotionState.NOT_PROMOTED
    
    def set_new_rank(self, new_rank: Rank):
        self.set_rank(new_rank)
       
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, PawnToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
