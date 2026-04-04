# src/model/token/model/concrete/king/king.py

"""
Module: model.token.model.concrete.king.king
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from model.coord import CoordDatabase
from model.rank import King
from model.team import Team
from model.token import Token, TokenBoardState, ReadinessState


class KingToken(Token):
    """
    Role:
        -   Model
        -   Data-Holder

    Responsibilities:
        1. Represent a piece with a king's rank.

    Attributes:
        id: int
        team: Team
        rank: Rank
        designation: str
        roster_number: int
        positions: CoordDatabase
        opening_square_name: str
        current_position: Optional[Coord]
        previous_address: Optional[Coord]
        token_board_state: TokenBoardState
        readiness_state: ReadinessState

    Provides:
        - is_checkmated() -> bool
        - is_active() -> bool
        - is_disabled() -> bool
        - is_in_check() -> bool

    Super Class:
        Token
    """

    def __init__(
            self,
            id: int,
            team: Team,
            designation: str,
            roster_number: int,
            opening_square_name: str,
            positions: CoordDatabase = CoordDatabase(),
    ):
        """
        Args:
            id: int
            team: Team
            designation: str
            roster_number: int
            opening_square_name: str
            positions: CoordDatabase
        """
        super().__init__(
            id=id,
            team=team,
            rank=King(),
            designation=designation,
            roster_number=roster_number,
            opening_square_name=opening_square_name,
            positions=positions,
        )
     
    @property
    def is_in_check(self) -> bool:
        return (
                self.board_state == TokenBoardState.DEPLOYED_ON_BOARD and
                self.readiness_state == ReadinessState.IN_CHECK
        )
    
    @property
    def is_checkmated(self) -> bool:
        return (
                self.board_state == TokenBoardState.DEPLOYED_ON_BOARD and
                self.readiness_state == ReadinessState.CHECKMATED
        )
    
    @property
    def is_active(self) -> bool:
        return (
                (ReadinessState.FREE or ReadinessState.IN_CHECK) and
                self.board_state == TokenBoardState.DEPLOYED_ON_BOARD
        )
    
    @property
    def is_disabled(self) -> bool:
        return (
                self.is_checkmated or
                self.board_state == TokenBoardState.NEVER_BEEN_PLACED
        )
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, KingToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
