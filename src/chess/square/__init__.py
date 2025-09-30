# chess/square/__init__.py

"""
## PURPOSE
This package provides foundational objects for the chess board. It defines the `Square` class,
which serves as a data container for storing a discover's location, and a `SquareValidator` to ensure
the integrity of square objects.

## CORE CLASSES
* `Square`: A data-holding object representing a single square on a chessboard.
* `SquareValidator`: A class that validates the data and integrity of a `Square` object.

## USAGE
To use this package, import the desired classes and perform square-related operations.

>>> from chess.subject import Square, SquareValidator
>>> from chess.coord import Coord
>>> from chess.piece import Piece
>>>
>>>
>>> # Build a new Square at Coord(2, 1)
>>> coord = Coord(row=2, column=1)
>>> build_outcome = SquareBuilder.build(square_id=1, name="B2", coord=coord)
>>> if not build_outcome.is_success():
>>>    raise build_outcome.exception
>>> square = cast(Square, build_outcome.payload)
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
from .builder import SquareBuilder
from .validator import SquareValidator

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



