# src/chess/token/model/concrete/combatant/occupant.py

"""
Module: chess.token.model.concrete.combatant.occupant
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from chess.team import Team
from chess.rank import Rank
from chess.square import Square
from chess.token import CombatantActivityState, Token, TokenBoardState
from chess.token.activity.combatant.state import CombatantReadiness


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
    
    def __init__(
            self,
            id: int,
            rank: Rank,
            team: Team,
            designation: str,
            roster_number: int,
            opening_square: Square,
            activity: CombatantActivityState = CombatantActivityState(),
    ):
        super().__init__(
            id=id,
            team=team,
            rank=rank,
            designation=designation,
            roster_number=roster_number,
            opening_square=opening_square,
            activity=activity,
        )
        self._captor = None
        self.activity.state = CombatantActivityState
    
    @property
    def is_active(self) -> bool:
        return (
                self._captor is None and
                self.board_state == TokenBoardState.FORMED_ON_BOARD and
                self.activity.classification == CombatantReadiness.FREE
        )
    
    @property
    def is_disabled(self) -> bool:
        return not self.is_active

    @property
    def capture_is_activated(self) -> bool:
        return (
                self._captor is not None and
                self.board_state == TokenBoardState.FORMED_ON_BOARD and
                self.activity.classification == CombatantReadiness.CAPTURE_ACTIVATED
        )
    
    @property
    def has_hostage_manifest(self) -> bool:
        return (
                self._captor is not None and
                self.board_state == TokenBoardState.FORMED_ON_BOARD and
                self.activity.classification == CombatantReadiness.ISSUED_HOSTAGE_MANIFEST
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