# src/chess/piece/combatant/combatant.py

"""
Module: chess.piece.combatant.combatant
Author: Banji Lawal
Created: 2025-10-17
version: 1.0.0
"""

from typing import Callable, Optional, cast

from chess.piece import Piece
from chess.rank import Rank
from chess.team import Team


class CombatantPiece(Piece):
    """
    # ROLE: Data-Holding, C
  
    # RESPONSIBILITIES:
    1.  Concrete subclass of Piece
    2.  Indicate the Combatant should be removed from the board by setting its captor attribute.
  
    # PROVIDES:
    CombatantPiece
  
    # ATTRIBUTES:
        *   captor (Optional[Piece]): Enemy who captured the combatant.
    """
    _captor: Optional[Piece]
    
    def __init__(self, id: int, name: str, rank: Rank, team: Team):
        super().__init__(id, name, rank, team)
        self._captor = None
    
    @property
    def captor(self) -> Optional[Piece]:
        return self._captor
    
    @captor.setter
    def captor(self, captor: Piece):
        self._captor = captor
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, CombatantPiece):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
