# src/chess/system/config.py
"""
Module: chess.system.config
Author: Banji Lawal
Created: 2025-10-09

# SCOPE:
-------
***Limitation***: This module cannot prevent classes, processes or modules using `Vector`
    instances that pass sanity checks will not fail when using the validated `Vector`.
    Once client's processes might fail, experience service inconsistency or have other
    faults.
    Objects authenticated by `VectorValidator` might fail additional requirements
    a client has for a `Vector`. It is the client's responsibility to ensure the
    validated `Vector` passes and additional checks before deployment.

**Related Features**:
    `Coord` -> See `Coord`, `CoordBuilder`, `CoordValidator`, module[chess.visitor_coord],
    `Scalar` --> See `Scalar`, `ScalarValidator`, module[chess.vector],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Configuration

# PURPOSE:
---------
1. Constants used in the application

**Satisfies**: Consistency, Reliability.

# DEPENDENCIES:
---------------
From `chess.system`:
    `GameColor`

# CONTAINS:
----------
 * `VectorValidator`
"""

from chess.system import GameColor

__all__ = [
  'ROW_SIZE',
  'COLUMN_SIZE',
  'BOARD_DIMENSION',
  'MIN_NAME_LENGTH',
  'MAX_NAME_LENGTH',
  'KNIGHT_STEP_SIZE',
  'CELL_PX',
  'BORDER_PX',
  'SCREEN_COLOR',
  'SCREEN_WIDTH',
  'SCREEN_HEIGHT',
  'PYGAME_CAPTION',
  'PYGAME_FONT',
  'PYGAME_FONT_SIZE',
  'OPPOSITE_CELL_COLOR'
]

ROW_SIZE = 8
COLUMN_SIZE = 8

BOARD_DIMENSION = 8
MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 40

"""
  This is the number of steps moves in eit
  her the x or y graph.
  If team knight steps over two rows it must step one diagonal column 
  This gives 3 total rows traveled.

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





