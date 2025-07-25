from enum import Enum

from chess.common.constant import BOARD_DIMENSION
from chess.motion.quadrant import Quadrant


class TeamHome(Enum):
    NORTH = "North"
    SOUTH = "South"


    def first_home_row(self):
        if self == TeamHome.NORTH:
            return 0
        return BOARD_DIMENSION - 1

    def second_home_row(self):
        if self == TeamHome.SOUTH:
            return 1
        return BOARD_DIMENSION - 2

    def get_enemy_home(self):
        if self == TeamHome.NORTH:
            return TeamHome.SOUTH
        return TeamHome.NORTH

    def get_enemy_home_row(self):
        return self.get_enemy_home().first_home_row()

    def step_toward_enemy(self):
        if self == TeamHome.NORTH:
            return -1
        return 1

    def home_quadrant(self):
        if self == TeamHome.NORTH:
            return Quadrant.N
        return Quadrant.S