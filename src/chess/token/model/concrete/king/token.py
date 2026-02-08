# src/chess/token/model/concrete/king/king.py

"""
Module: chess.token.model.concrete.king.king
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from chess.rank import King
from chess.team import Team
from chess.token import Token, TokenBoardState, ReadinessState


class KingToken(Token):
    
    def __init__(
            self,
            id: int,
            team: Team,
            designation: str,
            roster_number: int,
            opening_square_name: str,
    ):
        super().__init__(
            id=id,
            team=team,
            rank=King(),
            designation=designation,
            roster_number=roster_number,
            opening_square_name=opening_square_name,
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
