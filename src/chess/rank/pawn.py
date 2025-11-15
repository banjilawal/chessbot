# src/chess/rank/pawn.py

"""
Module: chess.rank.pawn
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""

from chess.coord import Coord
from chess.pawn import PawnPiece
from chess.geometry import Quadrant
from chess.rank import Rank, RankSpec
from chess.system import LoggingLevelRouter


class Pawn(Rank):
  """"""
  
  def __init__(
          self,
          id: int = RankSpec.PAWN.id,
          name: str = RankSpec.PAWN.name,
          letter: str = RankSpec.PAWN.letter,
          ransom: int = RankSpec.PAWN.ransom,
          quota: int = RankSpec.PAWN.quota,
          quadrants: list[Quadrant] = RankSpec.PAWN.quadrants
  ):
    super().__init(
      id=id,
      name=name,
      letter=letter,
      ransom=ransom,
      quadrants=quadrants,
      quota=quota
    )
    
  @classmethod
  def compute_span(cls, piece: PawnPiece) -> [Coord]:
    """"""
    origin = piece.current_position
    if piece.positions.size() == 1:
      return cls._opening_span(origin)
    return cls._developed_span(origin)
  
  @classmethod
  @LoggingLevelRouter.monitor
  def _developed_span(cls, origin: Coord) -> [Coord]:
    """"""
    return [
      Coord(column=origin.column, row=origin.row+1),
      Coord(column=origin.column-1, row=origin.row+1),
      Coord(column=origin.column+1, row=origin.row+1),
    ]
  
  
  @classmethod
  @LoggingLevelRouter
  def _opening_span(cls, origin: Coord) -> [Coord]:
    """"""
    return [
      cls._developed_span(origin),
      Coord(column=origin.column, row=origin.row+2),
      Coord(column=origin.column - 1, row=origin.row + 2),
      Coord(column=origin.column + 1, row=origin.row + 2)
    ]