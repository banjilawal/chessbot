"""
Rank Validation Exception - Exceptions raised by RankValidators

PURPOSE:
    Rank validators throw the same sort of exceptions have the same source and naming scheme. Organzing them
    in their own validation exception pacakge is easier to manage.


CORE CLASSES:
    RankValidationExce[tion: Super class of RankValidation exceptions
    BishopValidationException: Wrapper for exceptions raised by Bishop validaor
    KingValidationException: Wrapper for exceptions raised by King validaor
    KnightValidationException: Wrapper for exceptions raised by Knightmethods
    PawnValidationException: Wrapper for exceptions raised by Pawn validaor
    RookValidationException: Wrapper for exceptions raised by Rook validaor
    QueenValidationException: Wrapper for exceptions raised by Queen validaor


USAGE:
    >>> from chess.rank.exception.validation
    >>> raise QueenValidationException(f"{method}: {QueenValidationException.DEFAULT_MESSAGE}")

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .invalid_rank import RankValidationException
from .invalid_king import KingValidationException
from .invalid_pawn import PawnValidationException
from .invalid_knight import KnightValidationException
from .invalid_bishop import BishopValidationException
from .invalid_rook import RookValidationException
from .invalid_queen import QueenValidationException


InvalidRank = RankValidationException
InvalidKing = KingValidationException
InvalidPawn = PawnValidationException
InvalidKnight = KnightValidationException
InvalidBishop = BishopValidationException
InvalidRook = RookValidationException
InvalidQueen = QueenValidationException


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
    "RankValidationException",
    "KingValidationException",
    "PawnValidationException",
    "KnightValidationException",
    "BishopValidationException",
    "RookValidationException",
    "QueenValidationException",
    
    # Aliases
    "InvalidRank",
    "InvalidKing",
    "InvalidPawn",
    "InvalidKnight",
    "InvalidBishop",
    "InvalidRook",
    "InvalidQueen",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info"
]