import sys

from src.common.game_color import GameColor


class GameDefault:
    MIN_ID: int = 1
    COLUMN_COUNT: int = 21
    ROW_COUNT: int = 21
    OCCUPANT_HEIGHT: int = 1
    OCCUPANT_LENGTH: int = 2

    CELL_PX: int = 80
    CELL_COLOR: GameColor = GameColor.LIGHT_SALMON_PINK
    CELL_BORDER_COLOR: GameColor = GameColor.LIGHT_GRAY_2
    CELL_BORDER_WIDTH: int = 2
    SCREEN_PADDING: int = 40

    PORTAL_COLOR: GameColor = GameColor.GREEN
    BOULDER_COLOR: GameColor = GameColor.BLUE_GRAY
    CRATE_COLOR: GameColor = GameColor.BLUE
    BOARD_COLOR: GameColor = GameColor.WHITE

    MIN_TRAVEL_DISTANCE: int = 1
    MAX_TRAVEL_DISTANCE: int = sys.maxsize
