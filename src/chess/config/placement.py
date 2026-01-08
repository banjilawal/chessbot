from enum import Enum
from typing import Optional

from chess.token.piece import Piece
from chess.team.schema import TeamSchema
from chess.rank.spec import RankSpec


class PlacementChart(Enum):
  def __new__(
      cls,
      piece_name: str,
      square_name: str,
      rank: RankSpec,
      side: TeamSchema
  ):
    obj = object.__new__(cls)
    obj._piece_name= piece_name
    obj._square_name = square_name
    obj._rank = rank
    obj._side = side
    return obj

  WHITE_KING_CASTLE = ("WC1", "A8", RankSpec.ROOK, TeamSchema.WHITE)
  WHITE_KING_KNIGHT = ("WN1", "B8", RankSpec.KNIGHT, TeamSchema.WHITE)
  WHITE_KING_BISHOP = ("WB1", "C8", RankSpec.BISHOP, TeamSchema.WHITE)
  WHITE_KING = ("WK", "D8", RankSpec.KING, TeamSchema.WHITE)
  WHITE_QUEEN = ("WQ", "E8", RankSpec.QUEEN, TeamSchema.WHITE)
  WHITE_QUEEN_BISHOP = ("WB2", "F8", RankSpec.BISHOP, TeamSchema.WHITE)
  WHITE_QUEEN_KNIGHT = ("WN2", "G8", RankSpec.KNIGHT, TeamSchema.WHITE)
  WHITE_QUEEN_CASTLE = ("WC2", "H8", RankSpec.ROOK, TeamSchema.WHITE)

  WHITE_PAWN_1 = ("WP1", "A7", RankSpec.PAWN, TeamSchema.WHITE)
  WHITE_PAWN_2 = ("WP2", "B7", RankSpec.PAWN, TeamSchema.WHITE)
  WHITE_PAWN_3 = ("WP3", "C7", RankSpec.PAWN, TeamSchema.WHITE)
  WHITE_PAWN_4 = ("WP4", "D7", RankSpec.PAWN, TeamSchema.WHITE)
  WHITE_PAWN_5 = ("WP5", "E7", RankSpec.PAWN, TeamSchema.WHITE)
  WHITE_PAWN_6 = ("WP6", "F7", RankSpec.PAWN, TeamSchema.WHITE)
  WHITE_PAWN_7 = ("WP7", "G7", RankSpec.PAWN, TeamSchema.WHITE)
  WHITE_PAWN_8 = ("WP8", "H7", RankSpec.PAWN, TeamSchema.WHITE)

  BLACK_KING_CASTLE = ("BC1", "A1", RankSpec.ROOK, TeamSchema.BLACK)
  BLACK_KING_KNIGHT = ("BN1", "B1", RankSpec.KNIGHT, TeamSchema.BLACK)
  BLACK_KING_BISHOP = ("BB1", "C1", RankSpec.BISHOP, TeamSchema.BLACK)
  BLACK_KING = ("BK", "D1", RankSpec.KING, TeamSchema.BLACK)
  BLACK_QUEEN = ("BQ", "E1", RankSpec.QUEEN, TeamSchema.BLACK)
  BLACK_QUEEN_BISHOP = ("BB2", "F1", RankSpec.BISHOP, TeamSchema.BLACK)
  BLACK_QUEEN_KNIGHT = ("BN2", "G1", RankSpec.KNIGHT, TeamSchema.BLACK)
  BLACK_QUEEN_CASTLE = ("BC2", "H1", RankSpec.ROOK, TeamSchema.BLACK)

  BLACK_PAWN_1 = ("BP1", "A2", RankSpec.PAWN, TeamSchema.BLACK)
  BLACK_PAWN_2 = ("BP2", "B2", RankSpec.PAWN, TeamSchema.BLACK)
  BLACK_PAWN_3 = ("BP3", "C2", RankSpec.PAWN, TeamSchema.BLACK)
  BLACK_PAWN_4 = ("BP4", "D2", RankSpec.PAWN, TeamSchema.BLACK)
  BLACK_PAWN_5 = ("BP5", "E2", RankSpec.PAWN, TeamSchema.BLACK)
  BLACK_PAWN_6 = ("BP6", "F2", RankSpec.PAWN, TeamSchema.BLACK)
  BLACK_PAWN_7 = ("BP7", "G2", RankSpec.PAWN, TeamSchema.BLACK)
  BLACK_PAWN_8 = ("BP8", "H2", RankSpec.PAWN, TeamSchema.BLACK)

  @property
  def piece_name(self) -> str:
    return self._piece_name

  @property
  def square_name(self) -> str:
    return self._square_name

  @property
  def rank(self) -> RankSpec:
    return self._rank

  @property
  def side(self) -> TeamSchema:
    return self._side


  def __str__(self) -> str:
    return (
      f"Placement[{self._piece_name} = square:{self._square_name}]"
    )


  def filter_by_side(side_name: str) -> ['WhiteBattleOrder']:
    matches = []

    for placement in PlacementChart:
      if placement.side.name.upper() == side_name.upper():
        matches.append(placement)
    return matches


  def filter_by_rank(rank_name: str) -> ['WhiteBattleOrder']:
    matches = []

    for placement in PlacementChart:
      if placement.rank.name.upper() == rank_name.upper():
        matches.append(placement)
    return matches


  def find_placement_by_piece(piece: Piece) -> Optional['WhiteBattleOrder']:

    for placement in PlacementChart:
      if placement.piece_name.upper() == token.name.upper():
        return placement
    return None


def main():
  # for placement in WhiteBattleOrder:
  #   print(placement)

  for placement in PlacementChart.filter_by_side(side_name="white"):
    print(placement)


if __name__ == "__main__":
  main()
