# src/domain/model/searchable/state/token/combatant/model.py

"""
Module: domain.model.searchable.state.token.combatant.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import CombatantReadiness, Formation, HomeSquare, Team, Token, Footstep


class CombatantToken(Token):
    """
    Role:
        - Stateful Data Holder

    Responsibilities:
        1.  Capturable Token.

    Attributes:

        is_enemy: bool
        captor: Optional[Token]
        
    Provides:

    Super Class:
        Token
    """
    _captor: Optional[Token]
    _readiness: CombatantReadiness
    
    def __init__(
            self,
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
            footstep: Optional[Footstep] | None = None
    ):
        """
        Args:
            id: int
            team: Team
            rank: Rank
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
        self._captor = None
        self._readiness = CombatantReadiness.OFF_BOARD
    
    @property
    def captor(self) -> Optional[Token]:
        return self._captor
    
    @captor.setter
    def captor(self, captor: Token):
        self._captor = captor
        
    @property
    def readiness(self) -> CombatantReadiness:
        return self._readiness
    
    @readiness.setter
    def readiness(self, other: CombatantReadiness):
        self._readiness = other
    
    @property
    def is_ready(self) -> bool:
        return (
                self.has_been_deployed and
                self._captor is None and
                self._readiness == CombatantReadiness.READY
        )
    
    @property
    def is_not_ready(self) -> bool:
        return not self.is_ready
    
    @property
    def is_captured(self) -> bool:
        return (
                self.is_deployed and
                self._captor is not None and
                self._readiness == CombatantReadiness.CAPTURED
        )
    
   
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, CombatantToken):
                return self.id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)