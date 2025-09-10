"""
Geometry Package - Spatial Relationships in 2D Plane

PURPOSE:
    Provides classes for spatial relationships, coordinates, vectors, and paths
    in a 2D chess board coordinate system.

CORE CLASSES:
    Coord: Immutable (row, column) coordinate tuple for board positions
    Vector: Offset transformation (x, y) for coordinate movement
    Scalar: Single value with bounds checking for geometric operations
    Path: Directed path between two coordinates with line type classification
    Quadrant: Board subdivision for spatial partitioning

LINE TYPES (Line enum):
    VERTICAL, DIAGONAL, HORIZONTAL, KING, KNIGHT, BISHOP, CASTLE, QUEEN,
    PAWN_OPENING, PAWN_ADVANCE, PAWN_ATTACK, CURVILINEAR

USAGE:
    >>> from chess.geometry import Coord, Vector, Path, Line
    >>> start = Coord(1, 2)
    >>> end = Coord(3, 4)
    >>> vector = Vector(2, 2)
    >>> path = Path(start, end)
    >>> new_pos = start + vector  # Coord(3, 4)

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Include subpackages
from . import exception
from . import validator

# Core geometry classes
from .coord import Coord
from .vector import Vector
from .scalar import Scalar
from .line import Line
from .path import Path
from .quadrant import Quadrant


# Package metadata
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "geometry"


# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }


__all__ = [
    # Core classes
    "Coord",
    "Vector",
    "Scalar",
    "Path",
    "Quadrant",
    "Line",

    # Subpackage
    "exception",


    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info"
]