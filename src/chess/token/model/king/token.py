# src/chess/token/model/king/token.py

"""
Module: chess.token.model.king.token
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.rank import King
from chess.square import Square
from chess.team import Team
from chess.token import KingActivityState, Token, TokenBoardState


class KingToken(Token):
    _activity_state: KingActivityState
    
    def __init__(self, id: int, designation: str, roster_number: int, team: Team, opening_square: Square):
        super().__init__(
            id=id,
            designation=designation,
            roster_number=roster_number,
            rank=King(), team=team,
            opening_square=opening_square
        )
        self._activity_state = KingActivityState.FREE
        
    @property
    def activity_state(self) -> KingActivityState:
        return self._activity_state
    
    @activity_state.setter
    def activity_state(self, state: KingActivityState):
        self._activity_state = state
     
    @property
    def is_in_checked(self) -> bool:
        return (
                self.board_state == TokenBoardState.FORMED_ON_BOARD and
                self._activity_state == KingActivityState.IN_CHECK
        )
    
    @property
    def is_checkmated(self) -> bool:
        return (
                self.board_state == TokenBoardState.FORMED_ON_BOARD and
                self._activity_state == KingActivityState.CHECKMATED
        )
    
    @property
    def is_active(self) -> bool:
        return (
            self.board_state == TokenBoardState.FORMED_ON_BOARD and
            self._activity_state != KingActivityState.FREE
        )
    
    @property
    def is_disabled(self) -> bool:
        return self.board_state == TokenBoardState.NEVER_BEEN_PLACED or self.is_checkmated

    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, KingToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
