from enum import Enum

from chess.common.game_color import GameColor
from chess.geometry.quadrant import Quadrant
from chess.player.player_order import PlayerOrder
from chess.rank.rank_config import RankConfig


class TeamConfig(Enum):
    def __new__(
        cls,
        acronym: str,
        player_order: PlayerOrder,
        game_color: GameColor,
        back_row_index: int,
        pawn_row_index: int,
        home_quadant: Quadrant
    ):
        obj = object.__new__(cls)
        obj._acronym = acronym
        obj._player_order = player_order
        obj._acronym = acronym
        obj._game_color = game_color
        obj._back_row_index = back_row_index
        obj._pawn_row_index = pawn_row_index
        return obj

    WHITE = ("W", GameColor.WHITE, 0, 1, Quadrant.N)
    BLACK = ("B", GameColor.BLACK, 7, 6, Quadrant.S)


    @property
    def acronym(self) -> str:
        return self._acronym

    @property
    def game_color(self) -> GameColor:
        return self._game_color

    @property
    def back_rank_index(self) -> int:
        return self._back_row_index

    @property
    def pawn_rank_index(self) -> int:
        return self._pawn_row_index

    @property
    def quadrant(self) -> Quadrant:
        return self._quadrant