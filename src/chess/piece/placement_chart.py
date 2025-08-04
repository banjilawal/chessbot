from enum import Enum
from typing import List

from chess.player.player_config import PlayerConfig
from chess.rank.rank_config import RankConfig


class PlacementChart(Enum):
    def __new__(
            cls,
            acronym: str,
            player_order: PlayerOrder,
            game_color: GameColor,
            back_row_index: int,
            pawn_row_index: int,

    ):