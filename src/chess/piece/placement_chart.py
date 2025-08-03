from enum import Enum
from typing import List

from chess.player.player_config import PlayerConfig
from chess.rank.rank_config import RankConfig


class PlacementChart(Enum):
    def __new__(
            cls,
            acronym: str,
            rank_config: RankConfig,
            player_config: PlayerConfig,
            start_positions: List[str],
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