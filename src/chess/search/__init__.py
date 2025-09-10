"""
Search Package - Search Entities

PURPOSE:
    Separates search responsibilites from state mamangement, and data holding object.

CORE CLASSES:
    PieceSearch
    SquareSearch
    SideSearch
    SearchResult

USAGE:
    >>> from chess.search import PieceSerach, SearchResult
    >>> search_result = PieceSearch.by_name("BN2", [white_team, black_team])
    >>> if search_result.is_success():
    >>>     return cast(Piece, search_result.payload)

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Include search exceptions
from . import exception

# Core search classes
from .piece_search import PieceSearch
from .square_serch import SquareSearch
from .side_search import  SideSearch
from .search_result import SearchResult

# Class Aliases

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "search_pkg"


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
    "PieceSearch",
    "SquareSearch",
    "SideSearch",
    "SearchResult",

    # Aliases

    "__version__",
    "__author__",
    "package_info"
]