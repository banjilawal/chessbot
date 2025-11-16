# src/chess/rank/pawn.py

"""
Module: chess.rank.pawn
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""

from chess.coord import Coord, CoordService
from chess.pawn import PawnPiece
from chess.geometry import Quadrant
from chess.rank import Rank, RankSpec
from chess.system import LoggingLevelRouter


class Pawn(Rank):
  """
  # ROLE: Computation, Metadata

  # RESPONSIBILITIES:
  1.  Produces a list of Coords reachable from a Pawn's current position.
  2.  Metadata about the Pawn rank.

  # PROVIDES:
  Queen

  # ATTRIBUTES:
  See super class
  """
  
  def __init__(
          self,
          id: int = RankSpec.PAWN.id,
          name: str = RankSpec.PAWN.name,
          ransom: int = RankSpec.PAWN.ransom,
          team_quota: int = RankSpec.PAWN.team_quota,
          designation: str = RankSpec.PAWN.designation,
          quadrants: list[Quadrant] = RankSpec.PAWN.quadrants,
          coord_service: CoordService = CoordService()
  ):
    super().__init(
      id=id,
      name=name,
      ransom=ransom,
      quota=team_quota,
      letter=designation,
      quadrants=quadrants,
      coord_service=coord_service,
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