"""
Board Package -

PURPOSE:
    Board related classes

CORE CLASSES:
    Board, SquareIterator

CONVENIENCE ALIASES:


USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Subpackage imports
from .exception import *

# Core class
from .board import Board
from .square_iterator import SquareIterator


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.board"





# Export control - only what belongs in public API
__all__ = [
    # Core classes
    "Board",
    "SquareIterator",

    "NullBoardException",
    "FailedPieceRemovalException",
    "IncompleteBoardTransactionException",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info",
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

