# chess/rank/exception/__init__.py

"""
A package providing a structured hierarchy of exceptions for piece rank logic.

## PURPOSE
This package defines specific exceptions for issues encountered during a piece's movement or promotion
validation. This granular approach helps to quickly diagnose and resolve problems by pinpointing the
exact nature of the error, such as an invalid move for a specific piece type. Each exception acts as a
wrapper for underlying errors, providing a clean and consistent API for handling movement-related failures.

## CORE CLASSES
* `RankException`: The base exception for all rank-related errors.
* `BishopException`: A wrapper exception for errors raised during bishop movement validation.
* `KingException`: A wrapper exception for errors raised during king movement validation.
* `KnightException`: A wrapper exception for errors raised during knight movement validation.
* `PawnException`: A wrapper exception for errors raised during pawn movement validation.
* `RookException`: A wrapper exception for errors raised during rook movement validation.
* `QueenException`: A wrapper exception for errors raised during queen movement validation.
* `PromotionRowException`: Raised when a piece attempts to promote outside the designated promotion row.
* `UnpromotableException`: Raised when a piece that is not promotable attempts to be promoted.

## USAGE
These exceptions are typically raised within a `Rank` class's movement methods and can be caught to handle
invalid moves gracefully.

>>> from chess.rank.exception import PawnException
>>>
>>> def move_pawn(start_pos, end_pos):
...     # ... some validation logic
...     if not is_valid_pawn_move:
...         raise PawnException("Pawn cannot move in this way.")
...
>>> try:
...     move_pawn(start_coord, end_coord)
... except PawnException as e:
...     print(f"Invalid Pawn Move: {e}")

---
VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .move import *
from .validation import *

from .bishop_exception import BishopException
from .king_exception import KingException
from .knight_exception import KnightException
from .pawn_exception import PawnException
from .rook_exception import RookException
from .queen_exception import QueenException
from .promotion_row import PromotionRowException
from .unpromotable_exception import UnPromotableException

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.rank.exception"

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    "BishopException",
    "KnightException",
    "PawnException",
    "RookException",
    "KingException",
    "QueenException",
    "UnPromotableException",
    "PromotionRowException"

   *validation.__all__,
    "validation",

    *move.__all__,
    "move",

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