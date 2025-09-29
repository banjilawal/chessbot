# src/chess/geometry/__init__.py

"""
PURPOSE:
    Provides classes for spatial relationships, coordinates, vectors, and paths
    in a 2D chess board coordinate transaction.

CORE CLASSES:
    Line: Different types of edges
    Path: Directed path between two coordinates with line type classification
    Quadrant: Board subdivision for spatial partitioning

LINE TYPES (Line enum):
    VERTICAL, DIAGONAL, HORIZONTAL, KING, KNIGHT, BISHOP, CASTLE, QUEEN,
    PAWN_OPENING, PAWN_ADVANCE, PAWN_ATTACK, CURVILINEAR

USAGE:
    >>> from chess.geometry import Path, Line
    >>> path = Path(u=Coord(0,0), v=Coord(0,5))
    >>> path.line = Line.VERTICAL
    >>> return path.is_vertical()

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Core geometry classes
from .line import Line
from .path import Path
from .quadrant import Quadrant

# Package metadata
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.geometry"

__all__ = [
    # Core classes
    "Path",
    "Quadrant",
    "Line",

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
