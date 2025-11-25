# src/chess/piece/combatant/pawn/piece.py

"""
Module: chess.piece.combatant.pawn.piece
Author: Banji Lawal
Created: 2025-11-23
version: 1.0.0
"""


from typing import Optional

from chess.rank import Rank
from chess.team import Team
from chess.piece import CombatantPiece


class PawnPiece(CombatantPiece):
  
  _previous_rank: Optional[Rank]

  def __init__(self, id: int, name: str, rank: Rank, team: Team):
    super().__init__(id, name, rank, team)
    self._previous_rank = None
    
  @property
  def previous_rank(self) -> Optional[Rank]:
    return self._previous_rank
    
  def promote(self, new_rank: Rank):
    self._set_rank(new_rank)


  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, PawnPiece):
        return True
    return False

  def __hash__(self):
    return hash(self._id)



