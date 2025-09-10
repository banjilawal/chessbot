"""
 Square Exception Package

PURPOSE:
    Exceptions organic to Sqaure class

CORE CLASSES:
    NullSQuareException: Raised when a class or method recieves a null square
    SquareVaidationException: Raised if Square  fals validation vhecks
    

USAGE:
    >>> from chess.square.exception import NullSquare, SquareValidator
    >>>


VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Core square.exception classes

from .null import NullSquareException
from .invalid import SquareValidationException

# Class Aliases
NullSquare = NullSquareException
InvalidSquare = SquareValidationException

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "square_exception_pkg"


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
    "NullSquareException",
    "SquareValidationException",

# Aliases
    "NullSquare",
    "InvalidSquare",

    "__version__",
    "__author__",
    "package_info"
]