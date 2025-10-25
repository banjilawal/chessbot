# src/chess/piece/model/promotable/pawn.py

"""
Module: chess.piece.model.promotable.pawn
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""

from chess.rank import Rank
from chess.team import Team
from chess.piece import CombatantPiece, PromotablePiece

class PawnPiece(CombatantPiece, PromotablePiece):

  def __init__(self, id: int, name: str, rank: Rank, team: Team):
    super().__init__(id, name, rank, team)


  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, PawnPiece):
        return True
    return False

  def __hash__(self):
    return hash(self._id)



