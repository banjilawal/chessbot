# src/chess/pawn/rank.py

"""
Module: chess.pawn.rank
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""

from chess.coord import Coord
from chess.pawn import PawnPiece
from chess.rank import  Rank, RankSpec

class Pawn(Rank):
  """"""

  def __init__(self, spec: RankSpec=RankSpec.PAWN):
    super().__init__(
      id=spec.id,
      name=spec.name,
      letter=spec.letter,
      ransom=spec.ransom,
      quadrants=spec.quadrants,
      quota=spec.quota
    )
    
  @classmethod
  def compute_span(cls, piece: PawnPiece) -> [Coord]:
    """"""
    origin = piece.current_position
    if piece.positions.size() == 1:
      return cls._opening_span(origin)
    return cls._developed_span(origin)
  
  @classmethod
  def _developed_span(cls, origin: Coord) -> [Coord]:
    """"""
    return [
      Coord(column=origin.column, row=origin.row+1),
      Coord(column=origin.column-1, row=origin.row+1),
      Coord(column=origin.column+1, row=origin.row+1),
    ]
  
  
  @classmethod
  def _opening_span(cls, origin: Coord) -> [Coord]:
    """"""
    return [
      cls._developed_span(origin),
      Coord(column=origin.column, row=origin.row+2),
      Coord(column=origin.column - 1, row=origin.row + 2),
      Coord(column=origin.column + 1, row=origin.row + 2)
    ]