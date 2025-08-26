from enum import auto, Enum

from chess.common.color import GameColor

class MousePlacementStatus(Enum):
    PLACED = auto()
    BLOCKED = auto()
    RELEASED = auto()
    INVALID = auto()

BOARD_DIMENSION = 8
ROW_SIZE = 8
COLUMN_SIZE = 8

"""
    This is the number of steps moves in either the x or y domain.
    If a knight steps over two rows it must step one diagonal column 
    This gives 3 toal rows traveled.
    
    On the other hand if it steps over two columns it must step one diagonal row
    This also gives 3 total columns traveled.
    
    So KNIGHT_STEP_SIZE is 3
"""
KNIGHT_STEP_SIZE = 3

CELL_PX = 80
BORDER_PX = 2
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
PYGAME_CAPTION = "ChessBot"
PYGAME_FONT = "monospace"
PYGAME_FONT_SIZE = 150

SCREEN_COLOR = GameColor.DARK_GRAY_1.value
CELL_COLOR = GameColor.LIGHT_SAND.value
OPPOSITE_CELL_COLOR = SCREEN_COLOR

KING_COLOR = GameColor.OLIVE.value
PAWN_COLOR = GameColor.DEEP_ORANGE.value
KNIGHT_COLOR = GameColor.CERULEAN.value
BISHOP_COLOR = GameColor.INDIGO.value
CASTLE_COLOR = GameColor.SALMON.value
QUEEN_COLOR = GameColor.SILVER.value