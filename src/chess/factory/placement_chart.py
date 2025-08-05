from enum import Enum

from chess.team.team_config import TeamConfig
from chess.rank.rank_config import RankConfig


class PlacementChart(Enum):
    def __new__(
            cls,
            chess_piece_name: str,
            square_name: [str],
            rank_config: RankConfig,
            team_config: TeamConfig
    ):
        obj = object.__new__(cls)
        obj._value = chess_piece_name
        obj._square_name = square_name
        obj._rank_config = rank_config
        obj._team_config = team_config
        return obj

    WHITE_KING_CASTLE = ("WC1", "A8", RankConfig.CASTLE, TeamConfig.WHITE)
    WHITE_KING_KNIGHT = ("WN1", "B8", RankConfig.KNIGHT, TeamConfig.WHITE)
    WHITE_KING_BISHOP = ("WB1", "C8", RankConfig.BISHOP, TeamConfig.WHITE)
    WHITE_KING = ("WQ""D8", RankConfig.QUEEN, TeamConfig.WHITE)
    WHITE_QUEEN = ("E8", RankConfig.QUEEN, TeamConfig.WHITE)
    WHITE_QUEEN_BISHOP = ("F8", RankConfig.BISHOP, TeamConfig.WHITE)
    WHITE_QUEEN_KNIGHT = ("G8", RankConfig.KNIGHT, TeamConfig.WHITE)
    WHITE_QUEEN_CASTLE = ("H8", RankConfig.CASTLE, TeamConfig.WHITE)

    WHITE_PAWN_1 = ("A7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_2 = ("B7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_3 = ("C7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_4 = ("D7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_5 = ("E7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_6 = ("F7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_7 = ("G7", RankConfig.PAWN, TeamConfig.WHITE)
    WHITE_PAWN_8 = ("H7", RankConfig.PAWN, TeamConfig.WHITE)

    BLACK_KING_CASTLE = ("A1", RankConfig.CASTLE, TeamConfig.BLACK)
    BLACK_KING_KNIGHT = ("B1", RankConfig.KNIGHT, TeamConfig.BLACK)
    BLACK_KING_BISHOP = ("C1", RankConfig.BISHOP, TeamConfig.BLACK)
    BLACK_KING = ("D1", RankConfig.QUEEN, TeamConfig.BLACK)
    BLACK_QUEEN = ("E1", RankConfig.QUEEN, TeamConfig.BLACK)
    BLACK_QUEEN_BISHOP = ("F1", RankConfig.BISHOP, TeamConfig.BLACK)
    BLACK_QUEEN_KNIGHT = ("G1", RankConfig.KNIGHT, TeamConfig.BLACK)
    BLACK_QUEEN_CASTLE = ("H1", RankConfig.CASTLE, TeamConfig.BLACK)

    BLACK_PAWN_1 = ("A2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_2 = ("B2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_3 = ("C2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_4 = ("D2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_5 = ("E2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_6 = ("F2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_7 = ("G2", RankConfig.PAWN, TeamConfig.BLACK)
    BLACK_PAWN_8 = ("H2", RankConfig.PAWN, TeamConfig.BLACK)
