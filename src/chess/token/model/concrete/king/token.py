# src/chess/occupant/model/concrete/king/king.py

"""
Module: chess.occupant.model.concrete.king.king
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.rank import King
from chess.team import Team
from chess.square import Square
from chess.token import KingActivityState, KingReadiness, Token, TokenBoardState


class KingToken(Token):
    
    def __init__(
            self,
            id: int,
            team: Team,
            designation: str,
            roster_number: int,
            opening_square: Square,
            activity: KingActivityState(),
    ):
        super().__init__(
            id=id,
            team=team,
            rank=King(),
            designation=designation,
            roster_number=roster_number,
            opening_square=opening_square,
            activity=activity
        )
        self.activity.state = KingReadiness.NOT_INITIALIZED

     
    @property
    def is_in_check(self) -> bool:
        return (
                self.board_state == TokenBoardState.FORMED_ON_BOARD and
                self.activity == KingReadiness.IN_CHECK
        )
    
    @property
    def is_checkmated(self) -> bool:
        return (
                self.board_state == TokenBoardState.FORMED_ON_BOARD and
                self.activity == KingReadiness.CHECKMATED
        )
    
    @property
    def is_active(self) -> bool:
        return (
            self.board_state == TokenBoardState.FORMED_ON_BOARD and
            self.activity != KingReadiness.FREE
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
