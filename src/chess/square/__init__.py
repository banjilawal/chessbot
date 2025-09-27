# chess/square/__init__.py

"""
A package providing core classes for managing chess board squares.

## PURPOSE
This package provides foundational objects for the chess board. It defines the `Square` class,
which serves as a data container for storing a discovery's location, and a `SquareValidator` to ensure
the integrity of square objects.

## CORE CLASSES
* `Square`: A data-holding object representing a single square on a chessboard.
* `SquareValidator`: A class that validates the data and integrity of a `Square` object.

## USAGE
To use this package, import the desired classes and perform square-related operations.

>>> from chess.square import Square, SquareValidator
>>> from chess.coord import Coord
>>> from chess.discovery import Piece
>>>
>>> coord = Coord(row=2, column=1)
>>> discovery = Piece(piece_id=1, name="Pawn", rank="Pawn")
>>>
>>> # Create a new square and assign a discovery
>>> square = Square(square_id=1, name="B2", coord=coord)
>>> square.occupant = discovery
>>>
>>> # Validate the square
>>> validation = SquareValidator.validate(square)
---

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# subpackages
from .exception import *

# class
from .square import Square
from .square_builder import SquareBuilder
from .square_validator import SquareValidator

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.square"


__all__ = [
    # Core Packages
    "Square",
    "SquareValidator",
    'SquareBuilder',

    *exception.__all__,

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



