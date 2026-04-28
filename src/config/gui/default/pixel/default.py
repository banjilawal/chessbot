# src/config/gui/default/pixel/default.py

"""
Module: config.gui.default.pixel.default
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from system import GameDefault

__all__ = [
  "NUMBER_OF_ROWS",
  "NUMBER_OF_COLUMNS",
  "BOARD_PIXEL",
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






