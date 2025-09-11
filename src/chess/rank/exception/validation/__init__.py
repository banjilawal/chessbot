# chess/rank/exception/validation

"""
A package providing a structured hierarchy of exceptions for piece rank validation.

## PURPOSE
This package defines specific validation exceptions for each type of chess piece. By using a consistent naming
scheme, all piece rank validators provide a clean and predictable way to handle validation failures. The exceptions
are designed to pinpoint the exact piece type that caused the error, allowing for targeted error handling.

## CORE CLASSES
* `RankValidationException`: The base class for all rank validation exceptions.
* `BishopValidationException`: Raised when a bishop fails its validation checks.
* `KingValidationException`: Raised when a king fails its validation checks.
* `KnightValidationException`: Raised when a knight fails its validation checks.
* `PawnValidationException`: Raised when a pawn fails its validation checks.
* `RookValidationException`: Raised when a rook fails its validation checks.
* `QueenValidationException`: Raised when a queen fails its validation checks.

## USAGE
These exceptions are typically raised by a validator method and can be caught to handle invalid piece configurations
 gracefully.

>>> from chess.rank.exception.validation import KingValidationException
>>>
>>> def validate_king_move(king_piece, destination_coord):
...     # ... validation logic ...
...     if not is_valid_king_move:
...         raise KingValidationException("Invalid move for a king.")
...
>>> try:
...     validate_king_move(my_king, new_coord)
... except KingValidationException as e:
...     print(f"Validation Error: {e}")

---
VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Core exception imports
from .invalid_king import KingValidationException
from .invalid_knight import KnightValidationException
from .invalid_pawn import PawnValidationException
from .invalid_rook import RookValidationException
from .invalid_queen import QueenValidationException
from .invalid_bishop import BishopValidationException

# Package metadata
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.rank.exception.validation"

# Public API
__all__ = [
    # Core exceptions (alphabetical for clarity)
    "BishopValidationException",
    "KingValidationException",
    "KnightValidationException",
    "PawnValidationException",
    "QueenValidationException",
    "RookValidationException",

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
