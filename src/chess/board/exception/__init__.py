"""
Board.Exception Package - Subclasses of BoardException

PURPOSE:
    Exceptions raised by Board

CORE CLASSES:

CONVENIENCE ALIASES:


USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Subpackage imports


# Core package imports
from .null_board import NullBoardException
from .incomplete_transaction import IncompleteBoardTransactionException
from .piece_removal import FailedPieceRemovalException

# Aliases
NullBoard = NullBoardException
FailedPieceRemoval = FailedPieceRemovalException
IncompleteBoardTransaction = IncompleteBoardTransactionException

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "board_exception_pkg"


# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }


# Export control - only what belongs in public API
__all__ = [
    # Core classes
    "NullBoardException",
    "FailedPieceRemovalException",
    "IncompleteBoardTransactionException",

    # Aliases
    "NullBoard",
    "FailedPieceRemoval",
    "IncompleteBoardTransaction",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info"
]

