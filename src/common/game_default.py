import sys
from enum import Enum

from common.game_color import GameColor


class GameDefault:
    MIN_ID: int = 1
    COLUMN_COUNT: int = 8
    ROW_COUNT: int = 8
    OCCUPANT_HEIGHT: int = 1
    OCCUPANT_LENGTH: int = 2

    CELL_PX: int = 200
    CELL_COLOR: GameColor = GameColor.LIGHT_SALMON_PINK
    CELL_BORDER_COLOR: GameColor = GameColor.LIGHT_GRAY_2
    CELL_BORDER_WIDTH: int = 5

    PORTAL_COLOR: GameColor = GameColor.GREEN
    # BOULDER_COLOR: GameColor = GameColor.DARK_GRAY

    MIN_TRAVEL_DISTANCE: int = 1
    MAX_TRAVEL_DISTANCE: int = sys.maxsize
