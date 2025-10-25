"""
Module: piece
Author: Banji Lawal
Created: 2025-09-28
"""

from abc import ABC
from typing import Optional

from chess.rank import Rank
from chess.team import Team
from chess.piece import Piece


class PromotablePiece(Piece, ABC):
  """"""
  def __init__(self, id: int, name: str, rank: Rank, team: Team):
    super().__init__(id, name, rank, team)

  def promote_to_queen(self):
    self._rank = Queen
    
  
    
