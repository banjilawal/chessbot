# src/util/gui/default/color/default.py

"""
Module: util.gui.default.color.default
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from system import GameDefault

__all__ = [
  "NUMBER_OF_ROWS",
  "NUMBER_OF_COLUMNS",
  "BOARD_COLOR",
  "MIN_NAME_LENGTH",
  "MAX_NAME_LENGTH",
  "LONGEST_KNIGHT_LEG_SIZE",
  "CELL_PX",
  "BORDER_PX",
  "DEFAULT_DEFAULT",
  "DEFAULT_WIDTH",
  "DEFAULT_HEIGHT",
  "PYGAME_CAPTION",
  "PYGAME_FONT",
  "PYGAME_FONT_SIZE",
  "OPPOSITE_CELL_DEFAULT"
]

NUMBER_OF_ROWS = 8
NUMBER_OF_COLUMNS = 8

BOARD_COLOR = 8
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
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 800
PYGAME_CAPTION = "ChessBot"
PYGAME_FONT = "monospace"
PYGAME_FONT_SIZE = 150

DEFAULT_DEFAULT = GameDefault.DARK_GRAY_1.value
CELL_DEFAULT = GameDefault.LIGHT_SAND.value
OPPOSITE_CELL_DEFAULT = DEFAULT_DEFAULT





