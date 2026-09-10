# src/domain/model/searchable/state/token/combatant/pawn/model.py

"""
Module: domain.model.searchable.state.token.combatant.pawn.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from collection import CoordDatabase
from domain import (
    CombatantToken, DeploymentState, Formation, HomeSquare, Pawn, PromotionState, Rank,
    Team, Token, TokenReadiness
)


class PawnToken(CombatantToken):
    """
    Role:
        - Stateful Data Holder

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
        - set_new_rank(new_rank: Rank):
        
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
            rank: Optional[Rank] | None = None,
            captor: Optional[Token] | None = None,
            deployment_state: Optional[DeploymentState] | None = None,
            readiness: Optional[TokenReadiness] | None = None,
            positions: Optional[CoordDatabase] | None = None,
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
            rank=rank,
            captor=captor,
            formation=formation,
            readiness=readiness,
            home_square=home_square,
            deployment_state=deployment_state,
            positions=positions,
        )
        self._promotion_state = PromotionState.NOT_PROMOTED
    
    @property
    def promotion_state(self) -> PromotionState:
        return self._promotion_state
    
    @promotion_state.setter
    def promotion_state(self, promotion_state: PromotionState):
        self._promotion_state = promotion_state
        
    @property
    def is_promotable(self) -> bool:
        current_position = self.current_position
        
        if not self.is_active:
            return False
        if self.is_promoted:
            return False
        if current_position is None:
            return False
        if current_position.row != self.team.archetype.enemy_archetype.pawn_row:
            return False
        return True
    
    @property
    def is_not_promotable(self) -> bool:
        return not self.is_promotable
    
    @property
    def is_promoted(self) -> bool:
        return not isinstance(self.rank, Pawn)
    
    @property
    def is_not_promoted(self) -> bool:
        return not self.is_promoted
       
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, PawnToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
