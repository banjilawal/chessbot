from enum import Enum

from chess.common.game_color import GameColor
from chess.geometry.quadrant import Quadrant
from chess.team.play_order import PlayOrder


class TeamConfig(Enum):
    def __new__(
        cls,
        letter: str,
        player_order: PlayOrder,
        game_color: GameColor,
        back_row_index: int,
        pawn_row_index: int,
        home_quadrant: Quadrant
    ):
        obj = object.__new__(cls)
        obj._letter = letter
        obj._player_order = player_order
        obj._game_color = game_color
        obj._back_row_index = back_row_index
        obj._pawn_row_index = pawn_row_index
        obj._quadrant = home_quadrant
        return obj

    WHITE = ("W", PlayOrder.FIRST, GameColor.WHITE, 0, 1, Quadrant.N)
    BLACK = ("B", PlayOrder.SECOND, GameColor.BLACK, 7, 6, Quadrant.S)


    @property
    def letter(self) -> str:
        return self._letter


    @property
    def player_order(self) -> PlayOrder:
        return self._player_order

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