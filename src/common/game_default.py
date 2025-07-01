import sys
from enum import Enum

from common.game_color import GameColor


class GameDefault:
    MIN_ID: int = 1
    COLUMN_COUNT: int = 8
    ROW_COUNT: int = 8
    OBSTACLE_HEIGHT: int = 1
    OBSTACLE_LENGTH: int = 2

    CELL_PX: int = 400
    CELL_COLOR: GameColor = GameColor.LIGHT_SALMON_PINK
    OBSTACLE_COLOR: GameColor = GameColor.GRAY_2
    PORTAL_COLOR: GameColor = GameColor.GREEN

    MIN_TRAVEL_DISTANCE: int = 1
    MAX_TRAVEL_DISTANCE: int = sys.maxsize
