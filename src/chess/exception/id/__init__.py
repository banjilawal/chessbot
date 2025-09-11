"""
chess.exception.id Package

Purpose:
    id exceptions are thrown during validation. More granular than using numbers

Class:
    IdNullException: Id's cannot be null
    NegativeIdException: Ids must be positive

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .null_id_exception import IdNullException
from .negative_id_exception import NegativeIdException

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.exception.id"

__all__ = [
    "IdNullException",
    "NegativeIdException",

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
