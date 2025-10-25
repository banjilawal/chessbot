# src/chess/piece/model/promotable/promotable.py

"""
Module: chess.piece.model.promotable.promotable
Author: Banji Lawal
Created: 2025-10-24
version: 1.0.0
"""

from abc import ABC

from chess.team import Team
from chess.piece import Piece
from chess.rank import Rank, Queen

class PromotablePiece(Piece, ABC):
  """"""
  def __init__(self, id: int, name: str, rank: Rank, team: Team):
    super().__init__(id, name, rank, team)

  def promote_to_queen(self):
    self._set_rank(Queen())
    
  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, PromotablePiece):
        return True
    return False
  