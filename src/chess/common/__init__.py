"""
Common Package - Objects used frequently and globally accross packages

PURPOSE:
    Contains commonly used objects and utilites

CORE CLASSES:
    Event, Result, GameColor, MousePlacementStatus

CONVENIENCE ALIASES:
    MousePlacement: Alias for MousePlacementStatus

USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Subpackage imports
from . import exception

# Core package imports
from .permit import Event
from .result import Result
from .color import GameColor
from .validator import Validator
from .mouse import MousePlacementStatus

# Aliases
MousePlacement = MousePlacementStatus

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "common_pkg"


# Optional: Package-level constants
ROW_SIZE = 8
COLUMN_SIZE = 8

BOARD_DIMENSION = 8
MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 40

"""
    This is the number of steps moves in eit
    her the x or y domain.
    If a knight steps over two rows it must step one diagonal column 
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

# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }


# Export control - only what belongs in public API
__all__ = [
    # Core classes
    "Event",
    "Result",
    "GameColor",
    "Validator",
    "MousePlacementStatus",

    # Aliases
    "MousePlacement",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info",
]


