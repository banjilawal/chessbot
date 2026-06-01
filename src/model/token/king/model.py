# src/model/token/king/model.py

"""
Module: model.token.king.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model.coord import CoordDatabase

from model import OpeningSquare
from model.rank import King
from model.team import Team
from model.token import Token, TokenBoardState, TokenActivityState
from system import IdFactory


class KingToken(Token):
    """
    Role:
        -   Stateful Data-Holder

    Responsibilities:
        1. Token that can be checkmated not captured.

    Attributes:
        id: int
        team: Team
        rank: Rank
        designation: str
        roster_number: int
        positions: CoordDatabase
        opening_square: str
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

    def __init__(
            self,
            id: int,
            team: Team,
            designation: str,
            roster_number: int,
            opening_square: OpeningSquare,
    ):
        """
        Args:
            id: int
            team: Team
            designation: str
            roster_number: int
            opening_square: Square
        """
        rank = King(id=IdFactory.next_id(class_name="King"))
        super().__init__(
            id=id,
            team=team,
            rank=rank,
            designation=designation,
            roster_number=roster_number,
            opening_square=opening_square,
        )
     
    @property
    def is_in_check(self) -> bool:
        return (
                self.board_state == TokenBoardState.CLAIMED_HOME_SQUARE and
                self.readiness_state == TokenActivityState.IN_CHECK
        )
    
    @property
    def is_checkmated(self) -> bool:
        return (
                self.board_state == TokenBoardState.CLAIMED_HOME_SQUARE and
                self.readiness_state == TokenActivityState.CHECKMATED
        )
    
    @property
    def is_active(self) -> bool:
        return (
                (TokenActivityState.FREE or TokenActivityState.IN_CHECK) and
                self.board_state == TokenBoardState.CLAIMED_HOME_SQUARE
        )
    
    @property
    def is_disabled(self) -> bool:
        return (
                self.is_checkmated or
                self.board_state == TokenBoardState.HAS_NOT_DEPLOYED
        )
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, KingToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
