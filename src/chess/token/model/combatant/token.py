# src/chess/token/model/combatant/token.py

"""
Module: chess.token.model.combatant.token
Author: Banji Lawal
Created: 2025-10-17
version: 1.0.0
"""

from typing import Optional

from chess.square import Square
from chess.team import Team
from chess.rank import Rank
from chess.token import CombatantActivityStatue, Token, TokenBoardState


class CombatantToken(Token):
    """
    # ROLE: Data-Holding, C
  
    # RESPONSIBILITIES:
    1.  Concrete subclass of Token
    2.  Indicate the Combatant should be removed from the board by setting its victor attribute.
  
    # PROVIDES:
    CombatantToken
  
    # ATTRIBUTES:
        *   victor (Optional[Token]): Enemy who captured the combatant.
    """
    _captor: Optional[Token]
    _activity_state: CombatantActivityStatue
    
    def __init__(
            self,
            id: int,
            rank: Rank,
            team: Team,
            designation: str,
            roster_number: int,
            opening_square: Square,
    ):
        super().__init__(
            id=id,
            team=team,
            rank=rank,
            designation=designation,
            roster_number=roster_number,
            opening_square=opening_square
        )
        self._captor = None
        self._activity_state = CombatantActivityStatue.FREE
    
    @property
    def is_active(self) -> bool:
        return (
            self._captor is None and
            self.board_state == TokenBoardState.FORMED_ON_BOARD and
            self.activity_status != CombatantActivityStatue.FREE
        )
    
    @property
    def is_disabled(self) -> bool:
        return not self.is_active

    @property
    def is_captured(self) -> bool:
        return (
            self._captor is not None and
            self.board_state == TokenBoardState.FORMED_ON_BOARD and
            self.activity_status != CombatantActivityStatue.FREE
        )
    
    @property
    def activity_status(self) -> CombatantActivityStatue:
        return self._activity_state
    
    @activity_status.setter
    def activity_status(self, activity_status: CombatantActivityStatue):
        self._activity_state = activity_status
    
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
