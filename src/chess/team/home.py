from enum import Enum

from chess.common.config import BOARD_DIMENSION


class HomeOrientation(Enum):
    NORTH = "North"
    SOUTH = "South"

    def first_home_row(self):
        if self == HomeOrientation.NORTH:
            return 0
        return BOARD_DIMENSION - 1

    def second_home_row(self):
        if self == HomeOrientation.SOUTH:
            return 1
        return BOARD_DIMENSION - 2

    def get_enemy_home(self):
        if self == HomeOrientation.NORTH:
            return HomeOrientation.SOUTH
        return HomeOrientation.NORTH

    def get_enemy_home_row(self):
        return self.get_enemy_home().first_home_row()

    def step_toward_enemy(self):
        if self == HomeOrientation.NORTH:
            return -1
        return 1