from enum import Enum

from chess.common.color import GameColor
from chess.common.config import ROW_SIZE
from chess.geometry.quadrant import Quadrant
from chess.scalar import Scalar


class TeamProfile(Enum):

    def __new__(
        cls,
        game_color: GameColor,
        rank_row: int,
        advancing_step: Scalar,
        home_quadrant: Quadrant
    ):
        obj = object.__new__(cls)
        obj._game_color = game_color
        obj._rank_row = rank_row
        obj._advancing_step = advancing_step
        obj._home_quadrant = home_quadrant

        return obj

    WHITE = (GameColor.WHITE, 0, Scalar(1), Quadrant.N)
    BLACK = (GameColor.BLACK, (ROW_SIZE - 1), Scalar(-1), Quadrant.S)


    @property
    def letter(self) -> str:
        return self.name[0]


    @property
    def color(self) -> GameColor:
        return self._game_color


    @property
    def advancing_step(self) -> Scalar:
        return self._advancing_step

    @property
    def home_quadrant(self) -> Quadrant:
        return self.home_quadrant


    @property
    def rank_row(self) -> int:
        return self._rank_row


    @property
    def pawn_row(self) -> int:
        return self._rank_row + self._advancing_step.value


    @property
    def enemy_config(self) -> 'TeamProfile':
        return TeamProfile.BLACK if self == TeamProfile.WHITE else TeamProfile.WHITE


    def __str__(self) -> str:
        return (
            f"color:{self._game_color.name}, "
            f"advancing_step:{self._advancing_step} "
            f"rank_row:{self.rank_row} "
            f"pawn_row:{self.pawn_row}]"
        )


# def main():
#
#     for profile in TeamProfile:
#         print(profile)
#
#
# if __name__ == "__main__":
#     main()