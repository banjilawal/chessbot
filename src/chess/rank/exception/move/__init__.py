# chess/rank/exception/move/__init__.py

"""
A package providing a structured hierarchy of exceptions for invalid piece moves.

## PURPOSE
This package defines specific exceptions for each type of chess piece when its intended path of movement
doesn't meet the conditions of its rank. By using a consistent naming scheme (e.g., `BishopMovingException`),
the exceptions provide a clean and predictable way to handle move failures, helping developers to quickly
pinpoint the exact piece type that caused the error.

## CORE CLASSES
* `BishopMovingException`: Raised when a bishop's move path is invalid.
* `KingMovingException`: Raised when a king's move path is invalid.
* `KnightMovingException`: Raised when a knight's move path is invalid.
* `PawnMovingException`: Raised when a pawn's move path is invalid.
* `QueenMovingException`: Raised when a queen's move path is invalid.
* `RookMovingException`: Raised when a rook's move path is invalid.

## USAGE
These exceptions are typically raised within a rank's `walk` method and can be caught to handle invalid moves
gracefully.

>>> from chess.rank.exception.move import KingMovingException
>>>
>>> def validate_king_move(king_piece, destination_coord):
...     # ... logic to check if the path is a valid king move ...
...     if not is_valid_move:
...         raise KingMovingException("Invalid move path for a king.")
...
>>> try:
...     validate_king_move(my_king, new_coord)
... except KingMovingException as e:
...     print(f"Move Error: {e}")

---
VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Core exception imports
from .invalid_bishop_move import BishopMovingException
from .invalid_king_move import KingMovingException
from .invalid_pawn_move import PawnMovingException
from .invalid_queen_move import QueenMovingException
from .invalid_rook_move import RookMovingException
from .invalid_knight_move import KnightMovingException

# Package metadata
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.rank.exception.move"

# Public API
__all__ = [
    # Core exceptions (alphabetical for clarity)
    "BishopMovingException",
    "KingMovingException",
    "KnightMovingException",
    "PawnMovingException",
    "QueenMovingException",
    "RookMovingException",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info",
]


# Organic utility function
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__,
    }
