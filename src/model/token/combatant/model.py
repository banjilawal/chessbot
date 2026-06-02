# src/model/token/combatant/model.py

"""
Module: model.token.combatant.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import OpeningSquare
from model.team import Team
from model.rank import Rank
from model.token import Token, DeploymentState, TokenActivityState


class CombatantToken(Token):
    """
    Role:
        -   Stateful Data Holder

    Responsibilities:
        1.  Capturable Token.

    Attributes:
        id: int
        team: Team
        rank: Rank
        designation: str
        roster_number: int
        positions: CoordDatabase
        opening_square: OpeningSquare
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
    
    def __init__(
            self,
            id: int,
            rank: Rank,
            team: Team,
            designation: str,
            roster_number: int,
            opening_square: OpeningSquare,
    ):
        """
        Args:
            id: int
            team: Team
            rank: Rank
            designation: str
            roster_number: int
            opening_square: OpeningSquare
        """
        super().__init__(
            id=id,
            team=team,
            rank=rank,
            designation=designation,
            roster_number=roster_number,
            opening_square=opening_square,
        )
        self._captor = None
    
    @property
    def is_active(self) -> bool:
        return (
                self._captor is None and
                self.readiness_state == TokenActivityState.FREE and
                self.deployment_state == DeploymentState.CLAIMED_HOME_SQUARE
        )
    
    @property
    def is_disabled(self) -> bool:
        return not self.is_active

    @property
    def has_entered_hostage_process(self) -> bool:
        return (
                self._captor is not None and
                self.deployment_state == DeploymentState.CLAIMED_HOME_SQUARE and
                self.readiness_state == TokenActivityState.CAPTURE_ACTIVATED
        )
    
    @property
    def being_processed_as_hostage(self) -> bool:
        return (
                self._captor is not None and
                self.deployment_state == DeploymentState.REMOVED_FROM_BOARD and
                self.readiness_state == TokenActivityState.HOSTAGE_CREATED
        )
    
    @property
    def recorded_as_hostage(self) -> bool:
        return (
                self._captor is not None and
                self.deployment_state == DeploymentState.REMOVED_FROM_BOARD and
                self.readiness_state == TokenActivityState.HOSTAGE_IN_DATABASE
        )
    
    @property
    def captor(self) -> Optional[Token]:
        return self._captor
    
    @captor.setter
    def captor(self, captor: Token):
        self._captor = captor
        
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, CombatantToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)