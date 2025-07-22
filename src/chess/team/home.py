from enum import Enum

from chess.common.config import BOARD_DIMENSION


class HomeOrientation(Enum):
    NORTH = "North"
    SOUTH = "South"

    def first_home_row(self):
        if self == HomeOrientation.NORTH:
            return 0
        return BOARD_DIMENSION - 1

    def enemy_orientation(self):
        if self == HomeOrientation.NORTH:
            return HomeOrientation.SOUTH
        return HomeOrientation.NORTH

    def enemy_home_row(self):
        return self.enemy_orientation().first_home_row()

    def step_toward_enemy(self):
        if self == HomeOrientation.NORTH:
            return -1
        return 1