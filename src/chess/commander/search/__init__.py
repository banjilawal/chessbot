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
  # >>> from chess.search import PieceSerach, SearchResult
  # >>> search_result = BoardSearch.piece_by_name("BN2", [white_team, black_team])
  # >>> if search_result.is_success():
  # >>>   return cast(Piece, search_result.payload)


SEARCH EXCEPTIONS:
  Exceptions raised by Search entities

EXCEPTION CLASSES:
  PieceNotFoundException: Raised when team discover is not found by PieceSearch
  SqaureNotFoundException: Raised when team sqaure is not found by SquareSearch

USAGE:
  >>> from chess.search import BoardSearch  >>> from chess.search.team_exception import PieceNotFoundException
  >>> result = BoardSearch.piece_by_ide(1, [white_team, black_team)
  >>> if search_result.is_empty():
  >>>  raise PieceNotFoundException(f"{PieceNotFoundException.DEFAULT_MESSAGE}")


VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Core search classes
from chess.board.search import BoardSearch
from chess.team.search import TeamSearch
from .commander import CommanderSearch
from chess.system.search.result import SearchResult

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