"""
Search Package - Search Entities

PURPOSE:
    Separates search responsibilites from state mamangement, and data holding object.

CORE CLASSES:
    PieceSearch
    SquareSearch
    TeamSearch
    SearchResult

USAGE:
    >>> from chess.search import PieceSerach, SearchResult
    >>> search_result = BoardSearch.piece_by_name("BN2", [white_team, black_team])
    >>> if query_result.is_success():
    >>>     return cast(Piece, query_result.payload)

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Include search exceptions
from .exception import *

# Core search classes
from .board_search import BoardSearch
from .team_search import  TeamSearch
from .query_result import SearchResult

# Class Aliases

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.search"

__all__ = [
    # Core classes
    "BoardSearch",
    "TeamSearch",
    "SearchResult",

    # Subpackages
    *exception.__all__,
    "exception",

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