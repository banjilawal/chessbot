from enum import Enum

from chess.common.game_color import GameColor
from chess.piece.piece import ChessPiece
from chess.rank.rank_config import RankConfig


class PlayerConfig(Enum):
    def __new__(
            cls,
            acronym: str,
            game_color: GameColor,
            back_rank_index: int,
            pawn_rank_index: int,
            back_rank_layout: [RankConfig]
    ):
        obj = object.__new__(cls)
        obj._acronym = acronym
        obj._game_color = game_color
        obj._back_rank_index = back_rank_index
        obj._pawn_rank_index = pawn_rank_index
        obj._back_rank_layout = back_rank_layout
        return obj

    WHITE = ("W", GameColor.WHITE, 0, 1, [
        RankConfig.CASTLE, RankConfig.KNIGHT, RankConfig.BISHOP, RankConfig.QUEEN,
        RankConfig.KING, RankConfig.BISHOP, RankConfig.KNIGHT, RankConfig.CASTLE
    ])
    BLACK = ("B", GameColor.BLACK, 7, 6, [
        RankConfig.CASTLE, RankConfig.KNIGHT, RankConfig.BISHOP, RankConfig.QUEEN,
        RankConfig.KING, RankConfig.BISHOP, RankConfig.KNIGHT, RankConfig.CASTLE
    ])


    @property
    def acronym(self) -> str:
        return self._acronym

    @property
    def game_color(self) -> GameColor:
        return self._game_color

    @property
    def back_rank_index(self) -> int:
        return self._back_rank_index

    @property
    def pawn_rank_index(self) -> int:
        return self._pawn_rank_index