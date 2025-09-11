"""
Coord Package

PURPOSE:
    Immutable (row, column) coordinate tuple for board positions

CORE CLASSES:
    Coord:
    Coord_Stack:
    CoordValidator:

USAGE:
    >>> from chess.geometry.coord import Coord, CoordStack, CoordValidator
    >>>
    >>> coord = Coord(row=0, column=1)
    >>> coord_stack = CoordStack()
    >>> coord_stack.push_coord(coord)
    >>> validation = CoordValidator.validate(coord)

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Include subpackages
from .exception import *

# Core geometry classes
from .coord import Coord
from .coord_stack import CoordStack
from .coord_validator import CoordValidator
from .coord_stack_validator import CoordStackValidator

# Package metadata
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.coord"

__all__ = [
    # Core classes
    "Coord",
    "CoordStack",
    "CoordValidator",
    "CoordStackValidator",

    # Subpackage
    *exception.__all__,
    "exception",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info"
]

# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }