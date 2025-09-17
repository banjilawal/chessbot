"""
Chessexception Package - Project wide exceptions

PURPOSE:
    Contains core exceptions for entities. .


CORE CLASSES:
    PieceException: Supe class for exceptons raiedby Piece classes
    CombatantPiece: Concrete piece that can be captured
    KingPiece: Concrete king piece with special rules
    CoordStack: Coordinate history and management utility

Purpose:
    Name exceptions are thrown during validation. More granular than regular string checks

Class:
    BlankNameException
    NullNameException
    ShortNameException
    LongNameException
    IdNullException: Id's cannot be null
    NegativeIdException: Ids must be positive

USAGE:
    >>> from chess.exception import NullNameException
    >>> name = None
    >>> if name is None:
    >>>   raise NullNameException("Name cannot be null")

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .chess_exception import  *
from .collection_exception import *


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.exception"


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
    *chess_exception.__all__,
    *collection_exception.__all__,


    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info",
]