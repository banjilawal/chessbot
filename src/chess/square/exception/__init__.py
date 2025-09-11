# chess/square/exception/__init__.py

"""
A package providing a structured hierarchy of exceptions for square-related errors.

## PURPOSE
This package defines specific exceptions for issues encountered when interacting with `Square`
objects. This granular approach helps developers to quickly diagnose and resolve problems such
as a null square reference or a validation failure.

## CORE CLASSES
* `NullSquareException`: Raised when a method or function unexpectedly receives a `None` value
    instead of a `Square` instance.
* `SquareValidationException`: Raised when a `Square` object fails to meet its validation criteria.

## USAGE
These exceptions can be imported and raised from within the square-related code to enforce data integrity.

>>> from chess.square.exception import NullSquareException, SquareValidationException
>>> from chess.square import Square
>>> from chess.coord import Coord
>>>
>>> try:
...     # This will raise a NullSquareException
...     square = None
...     if square is None:
...         raise NullSquareException("Square reference cannot be null.")
... except NullSquareException as e:
...     print(f"Error: {e}")
...
>>> try:
...     # This will raise a SquareValidationException
...     coord = Coord(row=2, column=1)
...     square = Square(square_id=None, name="A1", coord=coord)
... except SquareValidationException as e:
...     print(f"Error: {e}")
---

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# --- core exceptions ---
from .null_square import NullSquareException
from .invalid_square import SquareValidationException

# --- metadata ---
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.square.exception"

# --- public API ---
__all__ = [
    "NullSquareException",
    "SquareValidationException",

    "__version__",
    "__author__",
    "package_info",
]

# --- utilities ---
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__,
    }
