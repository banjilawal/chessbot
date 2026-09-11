# src/domain/model/searchable/state/token/king/model.py

"""
Module: domain.model.searchable.state.token.king.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import CheckWarning, CheckmateAttack, TokenDeployment, Formation, HomeSquare, Team, Token, TokenReadiness



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
    _check_warning: Optional[CheckWarning]
    _checkmate: Optional[CheckmateAttack]
    

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
            formation=formation,
            home_square=home_square,
        )
        self._checkmate = None
        self._check_warning = None
        
    @property
    def checkmate(self) -> Optional[CheckmateAttack]:
        return self._checkmate
    
    @checkmate.setter
    def checkmate(self, other: CheckmateAttack):
        self._checkmate = other
        
    @property
    def check_warning(self) -> Optional[CheckWarning]:
        return self._check_warning
    
    @check_warning.setter
    def check_warning(self, other: CheckWarning):
        self._check_warning = other
        
    @property
    def is_ready(self) -> bool:
        return super().is_ready and
     
    @property
    def is_in_check(self) -> bool:
        return (
                self.
                self.readiness == TokenReadiness.IN_CHECK
        )
    
    @property
    def is_checkmated(self) -> bool:
        return (
                self.deployment == TokenDeployment.DEPLOYED_TO_HOME_SQUARE and
                self.readiness == TokenReadiness.CHECKMATED
        )
    
    @property
    def is_ready(self) -> bool:
        return (
                (
                        self.readiness == TokenReadiness.READY or
                        self.readiness == TokenReadiness.IN_CHECK
                ) and
                self.deployment == TokenDeployment.DEPLOYED_TO_HOME_SQUARE
        )
    
    @property
    def is_not_ready(self) -> bool:
        return (
                self.is_checkmated or
                self.deployment == TokenDeployment.NOT_DEPLOYED
        )
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, KingToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
