from enum import Enum
from typing import Optional

from chess.piece.piece import Piece
from chess.team.team_profile import TeamProfile
from chess.rank.profile import RankProfile


class PlacementChart(Enum):
    def __new__(
            cls,
            piece_name: str,
            square_name: str,
            rank: RankProfile,
            side: TeamProfile
    ):
        obj = object.__new__(cls)
        obj._piece_name= piece_name
        obj._square_name = square_name
        obj._rank = rank
        obj._side = side
        return obj

    WHITE_KING_CASTLE = ("WC1", "A8", RankProfile.CASTLE, TeamProfile.WHITE)
    WHITE_KING_KNIGHT = ("WN1", "B8", RankProfile.KNIGHT, TeamProfile.WHITE)
    WHITE_KING_BISHOP = ("WB1", "C8", RankProfile.BISHOP, TeamProfile.WHITE)
    WHITE_KING = ("WK", "D8", RankProfile.KING, TeamProfile.WHITE)
    WHITE_QUEEN = ("WQ", "E8", RankProfile.QUEEN, TeamProfile.WHITE)
    WHITE_QUEEN_BISHOP = ("WB2", "F8", RankProfile.BISHOP, TeamProfile.WHITE)
    WHITE_QUEEN_KNIGHT = ("WN2", "G8", RankProfile.KNIGHT, TeamProfile.WHITE)
    WHITE_QUEEN_CASTLE = ("WC2", "H8", RankProfile.CASTLE, TeamProfile.WHITE)

    WHITE_PAWN_1 = ("WP1", "A7", RankProfile.PAWN, TeamProfile.WHITE)
    WHITE_PAWN_2 = ("WP2", "B7", RankProfile.PAWN, TeamProfile.WHITE)
    WHITE_PAWN_3 = ("WP3", "C7", RankProfile.PAWN, TeamProfile.WHITE)
    WHITE_PAWN_4 = ("WP4", "D7", RankProfile.PAWN, TeamProfile.WHITE)
    WHITE_PAWN_5 = ("WP5", "E7", RankProfile.PAWN, TeamProfile.WHITE)
    WHITE_PAWN_6 = ("WP6", "F7", RankProfile.PAWN, TeamProfile.WHITE)
    WHITE_PAWN_7 = ("WP7", "G7", RankProfile.PAWN, TeamProfile.WHITE)
    WHITE_PAWN_8 = ("WP8", "H7", RankProfile.PAWN, TeamProfile.WHITE)

    BLACK_KING_CASTLE = ("BC1", "A1", RankProfile.CASTLE, TeamProfile.BLACK)
    BLACK_KING_KNIGHT = ("BN1", "B1", RankProfile.KNIGHT, TeamProfile.BLACK)
    BLACK_KING_BISHOP = ("BB1", "C1", RankProfile.BISHOP, TeamProfile.BLACK)
    BLACK_KING = ("BK", "D1", RankProfile.KING, TeamProfile.BLACK)
    BLACK_QUEEN = ("BQ", "E1", RankProfile.QUEEN, TeamProfile.BLACK)
    BLACK_QUEEN_BISHOP = ("BB2", "F1", RankProfile.BISHOP, TeamProfile.BLACK)
    BLACK_QUEEN_KNIGHT = ("BN2", "G1", RankProfile.KNIGHT, TeamProfile.BLACK)
    BLACK_QUEEN_CASTLE = ("BC2", "H1", RankProfile.CASTLE, TeamProfile.BLACK)

    BLACK_PAWN_1 = ("BP1", "A2", RankProfile.PAWN, TeamProfile.BLACK)
    BLACK_PAWN_2 = ("BP2", "B2", RankProfile.PAWN, TeamProfile.BLACK)
    BLACK_PAWN_3 = ("BP3", "C2", RankProfile.PAWN, TeamProfile.BLACK)
    BLACK_PAWN_4 = ("BP4", "D2", RankProfile.PAWN, TeamProfile.BLACK)
    BLACK_PAWN_5 = ("BP5", "E2", RankProfile.PAWN, TeamProfile.BLACK)
    BLACK_PAWN_6 = ("BP6", "F2", RankProfile.PAWN, TeamProfile.BLACK)
    BLACK_PAWN_7 = ("BP7", "G2", RankProfile.PAWN, TeamProfile.BLACK)
    BLACK_PAWN_8 = ("BP8", "H2", RankProfile.PAWN, TeamProfile.BLACK)

    @property
    def piece_name(self) -> str:
        return self._piece_name

    @property
    def square_name(self) -> str:
        return self._square_name

    @property
    def rank(self) -> RankProfile:
        return self._rank

    @property
    def side(self) -> TeamProfile:
        return self._side


    def __str__(self) -> str:
        return (
            f"Placement[{self._piece_name} = square:{self._square_name}]"
        )


    def filter_by_side(side_name: str) -> ['PlacementChart']:
        matches = []

        for placement in PlacementChart:
            if placement.side.name.upper() == side_name.upper():
                matches.append(placement)
        return matches


    def filter_by_rank(rank_name: str) -> ['PlacementChart']:
        matches = []

        for placement in PlacementChart:
            if placement.rank.name.upper() == rank_name.upper():
                matches.append(placement)
        return matches


    def find_placement_by_piece(piece: Piece) -> Optional['PlacementChart']:

        for placement in PlacementChart:
            if placement.piece_name.upper() == piece.name.upper():
                return placement
        return None


def main():
    # for placement in PlacementChart:
    #     print(placement)

    for placement in PlacementChart.filter_by_side(side_name="white"):
        print(placement)


if __name__ == "__main__":
    main()
