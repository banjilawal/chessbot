"""
Rank Exception - Exceptions thrown by Rank Subclasses

PURPOSE:
    Containts exceptions raised by Rank subclases. Any exceptions raised inside
    the class methods are wrapped in the RankException

CORE CLASSES:
    BishopException: Wrapper for exceptions raised by Bishop methods
    KingException: Wrapper for exceptions raised by King methods
    KnightException: Wrapper for exceptions raised by Knightmethods
    PawnException: Wrapper for exceptions raised by Pawn methods
    RookException: Wrapper for exceptions raised by Rook methods
    QueenException: Wrapper for exceptions raised by Queen methods
    PromotionRowException: Raised if class whose parent is not QueenPromotable tries getting promoted
    UnPromotableException: Raised if a QueenPromotable class tries to get promoted outside its enemy's rank row



USAGE:
    >>> from rankexception_pkg import QueenException
    >>> raise QueenException(f"{method}: {QueenException.DEFAULT_MESSAGE}")

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

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
__package_name__ = "rank_exception_package"



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
    "BishopException",
    "KnightException",
    "PawnException",
    "RookException",
    "KingException",
    "QueenException",
    "UnPromotableException",
    "PromotionRowException"
]