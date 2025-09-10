"""
 Team Exception Pacakge

PURPOSE:
    Exceptions raised by Team entities

CORE CLASSES:
    PieceNotFoundException: Raised when a piece is not found by PieceTeam
    SqaureNotFoundException: Raised when a sqaure is not found by SquareTeam

USAGE:
    >>> from chess.team import PieceTeam    >>> from chess.team.exception import PieceNotFoundException
    >>> result = PieceTeam.by_id(1, [white_team, black_team)
    >>> if result.is_not_found():
    >>>    raise PieceNotFoundException(f"{PieceNotFoundException.DEFAULT_MESSAGE}")


VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Core team.exception classes

from .piece_not_found import PieceNotFoundException
from .square_not_found import SquareNotFoundException

# Class Aliases
PieceNotFound = PieceNotFoundException
SquareNotFound = SquareNotFoundException

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "team_exception_pkg"


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
    "PieceNotFoundException",
    "SquareNotFoundException",

    # Aliases
    "PieceNotFound",
    "SquareNotFound",

    "__version__",
    "__author__",
    "package_info"
]