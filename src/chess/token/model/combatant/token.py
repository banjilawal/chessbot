# src/chess/token/model/combatant/token.py

"""
Module: chess.token.model.combatant.token
Author: Banji Lawal
Created: 2025-10-17
version: 1.0.0
"""

from typing import Optional

from chess.team import Team
from chess.rank import Rank
from chess.token import Token


class CombatantToken(Token):
    """
    # ROLE: Data-Holding, C
  
    # RESPONSIBILITIES:
    1.  Concrete subclass of Token
    2.  Indicate the Combatant should be removed from the board by setting its captor attribute.
  
    # PROVIDES:
    CombatantToken
  
    # ATTRIBUTES:
        *   captor (Optional[Token]): Enemy who captured the combatant.
    """
    _captor: Optional[Token]
    
    def __init__(self, id: int, name: str, rank: Rank, team: Team):
        super().__init__(id, name, rank, team)
        self._captor = None
    
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
