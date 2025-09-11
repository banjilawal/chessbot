"""
Coord Exception Package

PURPOSE:
    Immutable (row, column) coordinate tuple for board positions

CORE CLASSES:
    NullCoordException
    CoordValidationException

USAGE:
    >>> from chess.geometry.coord.exception import CoordValidationException
    >>> raise CoordValidationException("Invalid coord")

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .null import *

from .row_above_bounds import RowAboveBoundsException
from .row_below_bounds import RowBelowBoundsException
from .col_below_bounds import ColumnBelowBoundsException
from .col_above_bounds import ColumnAboveBoundsException
from .invalid_coord import CoordValidationException
from .invalid_coord_stack import CoordStackValidationException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.coord.exception"


__all__ = [
    # Core classes
    "RowBelowBoundsException",
    "RowAboveBoundsException",
    "ColumnBelowBoundsException",
    "ColumnAboveBoundsException",
    "CoordValidationException",
    "CoordStackValidationException",

    # Subpackages
    *null.__all__,
    "null",

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
