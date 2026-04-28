# src/config/gui/default/color/config.py

"""
Module: config.gui.default.color.config
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""



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

from dataclasses import dataclass
from typing import Any, Dict, Tuple


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

@dataclass
class DefaultGameColorSetting:
  settings: Dict[str, Any] = {
    "background": GameColor.DARK_GRAY_1.value,
    "opening_player": GameColor.IVORY.value,
    "following_player": GameColor.BLACK.value,
    "cell": GameColor.LIGHT_SAND.value,
    "default": GameColor.DARK_GRAY_1.value,
  }




