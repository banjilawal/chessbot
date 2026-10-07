# src/domain/model/searchable/state/token/combatant/pawn/model.py

"""
Module: domain.model.searchable.state.token.combatant.pawn.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import (
    Bishop, CombatantToken, Formation, HomeSquare, Knight, Pawn, Persona, PromotionState, Queen, Rank, Rook, Team, Footstep
)


class PawnToken(CombatantToken):
    """
    Role:
        - Stateful Data Holder

    Responsibilities:
        1.  Promotable combatant.

    Attributes:
        promotion_state: PromotionState

        is_promotable: bool
        is_promoted: bool
        is_not_promoted: bool
        
    Provides:
        
    Super Class:
        CombatantToken
    """
    _PROMOTION_PERSONAS = [
        Persona.BISHOP, Persona.KNIGHT, Persona.ROOK, Persona.QUEEN
    ]
    _PROMOTION_RANKS = (Bishop, Knight, Rook, Queen)
    
    _rank: Rank
    _promotion_persona: Persona
    _promotion_state: PromotionState
    
    def __init__(
            self,
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
            footstep: Optional[Footstep] | None = None,
    ):
        """
        Args:
            id: int
            team: Team
            formation: Formation
            home_square: OpeningSquare
            footstep: Optional[Footstep]
        """
        super().__init__(
            id=id,
            team=team,
            footstep=footstep,
            formation=formation,
            home_square=home_square,
        )
        self._rank = formation.rank
        self._promotion_persona = formation.rank.persona
        self._promotion_state = PromotionState.NOT_PROMOTED
    
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @rank.setter
    def rank(self, other: Rank):
        self._rank = other
        self._promotion_persona = other.persona
        
    @property
    def promotion_persona(self) -> Persona:
        return self._promotion_persona
    
    @property
    def promotion_state(self) -> PromotionState:
        return self._promotion_state
    
    @promotion_state.setter
    def promotion_state(self, promotion_state: PromotionState):
        self._promotion_state = promotion_state
        
    @property
    def is_promotable(self) -> bool:
        position = self.footstep.position
        
        if position is None:
            return False
        if self.is_not_ready:
            return False
        if self.is_promoted:
            return False
        if self.footstep.size < 2:
            return False
        if position.row != self.team.archetype.enemy_archetype.pawn_row:
            return False
        return True
    
    @property
    def is_not_promotable(self) -> bool:
        return not self.is_promotable
    
    @property
    def is_promoted(self) -> bool:
        return (
                isinstance(self._rank, self._PROMOTION_RANKS) and
                self._promotion_persona in self._PROMOTION_PERSONAS and
                self._promotion_state == PromotionState.PROMOTED
        )
    
    @property
    def is_not_promoted(self) -> bool:
        return (
            isinstance(self._rank, Pawn) and
            self._promotion_persona == Persona.PAWN and
            self._promotion_state == PromotionState.NOT_PROMOTED
        )
       
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, PawnToken):
                return self.id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
