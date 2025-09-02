from enum import Enum

from chess.common.color import GameColor
from chess.geometry.quadrant import Quadrant
from chess.geometry.vector.delta import Vector


class TeamConfig(Enum):

    def __new__(cls, game_color: GameColor, advancing_step: Vector, home_quadrant: Quadrant):
        obj = object.__new__(cls)
        obj._game_color = game_color
        obj._advancing_step = advancing_step
        obj._quadrant = home_quadrant

        return obj

    WHITE = (GameColor.WHITE, Vector(x=0, y=1), Quadrant.N)
    BLACK = (GameColor.BLACK, Vector(x=0, y=-1), Quadrant.S)


    @property
    def letter(self) -> str:
        return self.name[0]


    @property
    def color(self) -> GameColor:
        return self._game_color


    @property
    def rank_row(self) -> int:
        return self._quadrant.row


    @property
    def pawn_row(self) -> int:
        return self._quadrant.row + self._advancing_step.y


    @property
    def home_quadrant(self) -> Quadrant:
        return self._quadrant


    @property
    def enemy_quadrant(self) -> Quadrant:
        return self._quadrant.enemy_quadrant()

    def __str__(self) -> str:
        return (
            f"Quadrant[name:{self.name}, "
            f"color:{self._game_color.name}, "
            f"advancing_step:{self._advancing_step} "
            f"rank_row:{self.rank_row} "
            f"pawn_row{self.pawn_row}]"
        )

def main():
    conf = TeamConfig.WHITE
    print(conf)


if __name__ == "__main__":
    main()