# src/domain/model/searchable/state/token/king/model.py

"""
Module: domain.model.searchable.state.token.king.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import DeploymentState, Formation, HomeSquare, Team, Token, TokenReadiness


class KingToken(Token):
    """
    Role:
        - Stateful Data-Holder

    Responsibilities:
        1. Token that can be checkmated not captured.

    Attributes:
        id: int
        team: Team
        rank: Rank
        designation: str
        roster_number: int
        positions: CoordDatabase
        home_square: str
        current_position: Optional[Coord]
        previous_address: Optional[Coord]
        token_board_state: TokenBoardState
        readiness_state: TokenActivityState
        is_not_deployed: bool
        is_active(self): bool
        is_disabled: bool
        is_enemy: bool
        is_checkmated: bool
        is_active: bool
        is_disabled: bool
        is_in_checkk: bool

    Super Class:
        Token
    """
    _check_count: int
    

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
            formation: Formation
            home_square: Square
        """
        super().__init__(
            id=id,
            team=team,
            rank=King(),
            formation=formation,
            home_square=home_square,
        )
        self._check_count = 0
        
    @property
    def check_count(self) -> int:
        return self._check_count
    
    @check_count.setter
    def check_count(self, update):
        self._check_count = update
     
    @property
    def is_in_check(self) -> bool:
        return (
                self.deployment_state == DeploymentState.DEPLOYED and
                self.readiness == TokenReadiness.IN_CHECK
        )
    
    @property
    def is_checkmated(self) -> bool:
        return (
                self.deployment_state == DeploymentState.DEPLOYED and
                self.readiness == TokenReadiness.CHECKMATED
        )
    
    @property
    def is_active(self) -> bool:
        return (
                (
                        self.readiness == TokenReadiness.READY or
                        self.readiness == TokenReadiness.IN_CHECK
                ) and
                self.deployment_state == DeploymentState.DEPLOYED
        )
    
    @property
    def is_disabled(self) -> bool:
        return (
                self.is_checkmated or
                self.deployment_state == DeploymentState.NOT_DEPLOYED
        )
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, KingToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
