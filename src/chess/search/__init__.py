"""
Search Package - Search Entities

PURPOSE:
    Separates search responsibilites from state mamangement, and data holding object.

CORE CLASSES:
    EncounterSearch
    SquareSearch
    TeamSearch
    SearchResult

USAGE:
    >>> from chess.search import PieceSerach, SearchResult
    >>> search_result = BoardSearch.piece_by_name("BN2", [white_team, black_team])
    >>> if query_result.is_success():
    >>>     return cast(Piece, query_result.payload)


SEARCH EXCEPTIONS:
    Exceptions raised by Search entities

EXCEPTION CLASSES:
    PieceNotFoundException: Raised when a piece is not found by EncounterSearch
    SqaureNotFoundException: Raised when a sqaure is not found by SquareSearch

USAGE:
    >>> from chess.search import BoardSearch    >>> from chess.search.team_exception import PieceNotFoundException
    >>> result = BoardSearch.piece_by_ide(1, [white_team, black_team)
    >>> if result.is_not_found():
    >>>    raise PieceNotFoundException(f"{PieceNotFoundException.DEFAULT_MESSAGE}")


VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Core search classes
from .board import BoardSearch
from .team import  TeamSearch
from .commander import CommanderSearch
from .query_result import SearchResult

from .search_exception import (
    SearchException,
    PieceNotFoundException,
    SquareNotFoundException
)

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.search"

__all__ = [
    # Core classes
    "BoardSearch",
    "TeamSearch",
    'CommanderSearch',
    'SearchResult',

    "SearchException",
    "PieceNotFoundException",
    "SquareNotFoundException",

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