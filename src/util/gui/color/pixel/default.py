# src/util/gui/color/pixel/default.py

"""
Module: util.gui.color.pixel.default
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from system import GameColor

__all__ = [
  "NUMBER_OF_ROWS",
  "NUMBER_OF_COLUMNS",
  "BOARD_PIXEL",
  "MIN_NAME_LENGTH",
  "MAX_NAME_LENGTH",
  "LONGEST_KNIGHT_LEG_SIZE",
  "CELL_PX",
  "BORDER_PX",
  "COLOR_COLOR",
  "COLOR_WIDTH",
  "COLOR_HEIGHT",
  "PYGAME_CAPTION",
  "PYGAME_FONT",
  "PYGAME_FONT_SIZE",
  "OPPOSITE_CELL_COLOR"
]

NUMBER_OF_ROWS = 8
NUMBER_OF_COLUMNS = 8

BOARD_PIXEL = 8
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
COLOR_WIDTH = 800
COLOR_HEIGHT = 800
PYGAME_CAPTION = "ChessBot"
PYGAME_FONT = "monospace"
PYGAME_FONT_SIZE = 150

COLOR_COLOR = GameColor.DARK_GRAY_1.value
CELL_COLOR = GameColor.LIGHT_SAND.value
OPPOSITE_CELL_COLOR = COLOR_COLOR





