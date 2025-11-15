# src/chess/system/config.py

"""
Module: chess.system.config
Author: Banji Lawal
Created: 2025-09-16
"""

from chess.system import GameColor

__all__ = [
  "ROW_SIZE",
  "COLUMN_SIZE",
  "BOARD_DIMENSION",
  "MIN_NAME_LENGTH",
  "MAX_NAME_LENGTH",
  "LONGEST_KNIGHT_LEG_SIZE",
  "CELL_PX",
  "BORDER_PX",
  "SCREEN_COLOR",
  "SCREEN_WIDTH",
  "SCREEN_HEIGHT",
  "PYGAME_CAPTION",
  "PYGAME_FONT",
  "PYGAME_FONT_SIZE",
  "OPPOSITE_CELL_COLOR"
]

ROW_SIZE = 8
COLUMN_SIZE = 8

BOARD_DIMENSION = 8
MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 40

"""
  This is the number of steps moves in eit
  her the x or y graph.
  If team_name knight steps over two rows it must step one diagonal column
  This gives 3 total rows traveled.

  On the other hand if it steps over two columns it must step one diagonal row
  This also gives 3 total columns traveled.

  So LONGEST_KNIGHT_LEG_SIZE is2
"""
LONGEST_KNIGHT_LEG_SIZE = 2

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





