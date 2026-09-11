# src/domain/model/searchable/state/token/combatant/model.py

"""
Module: domain.model.searchable.state.token.combatant.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from collection import CoordDatabase
from domain import CombatantReadiness, TokenDeployment, Formation, HomeSquare, Team, Token, TokenReadiness


class CombatantToken(Token):
    """
    Role:
        - Stateful Data Holder

    Responsibilities:
        1.  Capturable Token.

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
            positions: Optional[CoordDatabase] | None = None,
    ):
        """
        Args:
            id: int
            team: Team
            rank: Rank
            formation: Formation
            home_square: OpeningSquare
        """
        super().__init__(
            id=id,
            team=team,
            formation=formation,
            home_square=home_square,
            positions=positions,
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
                self.is_deployed and
                self._captor is None and
                self._readiness == CombatantReadiness.READY
        )
    
    @property
    def is_not_ready(self) -> bool:
        return not self.is_ready or self.is_captured
    
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