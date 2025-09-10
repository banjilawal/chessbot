"""
Square Package

PURPOSE:
    Squares are occupied by Piece

CORE CLASSES:
    Square

USAGE:
    >>> from chess.square import Square
    >>> square = Square(square_id=1, name="B2", coord=coord)
    >>> square.occupant = piece
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# subpackages

# class
from .square import Square

# Class Aliases

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "square_pkg"


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
    # Core Packages
    "Square",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info"
]

