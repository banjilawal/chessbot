from enum import Enum

from common.game_color import GameColor


class GameDefault:
    MIN_ID = 1
    COLUMN_COUNT = 8
    ROW_COUNT = 8
    OBSTACLE_HEIGHT = 1
    OBSTACLE_LENGTH = 2

    CELL_PX = 400
    CELL_COLOR = GameColor.LIGHT_SALMON_PINK
    OBSTACLE_COLOR = GameColor.GRAY_2
    PORTAL_COLOR = GameColor.GREEN

    MIN_TRAVEL_DISTANCE = 1
    MAX_TRAVEL_DISTANCE = 45555
