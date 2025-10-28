"""
Search Package - Search Entities

PURPOSE:
  Separates old_search responsibilites from state mamangement, and service holding object.

CORE CLASSES:
  BoardPieceSearch
  SquareSearch
  BoardSearch
  SearchResult

USAGE:
  # >>> from chess.old_search import PieceSerach, SearchResult
  # >>> search_result = BoardSearch.piece_by_name("BN2", [white_team, black_team])
  # >>> if search_result.is_success():
  # >>>   return cast(Piece, search_result.payload)


SEARCH EXCEPTIONS:
  Exceptions raised by Search entities

EXCEPTION CLASSES:
  PieceNotFoundException: Raised when team discover is not found by BoardPieceSearch
  SqaureNotFoundException: Raised when team sqaure is not found by SquareSearch

USAGE:
  >>> from chess.old_search import BoardSearch  >>> from chess.old_search.team_exception import PieceNotFoundException
  >>> notification = BoardSearch.piece_by_ide(1, [white_team, black_team)
  >>> if search_result.is_empty():
  >>>  raise PieceNotFoundException(f"{PieceNotFoundException.DEFAULT_MESSAGE}")


VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Core old_search classes
from chess.board.search import BoardSearch
from chess.team.search import TeamSearch
from .commander import CommanderSearch
from chess.system.search.result import SearchResult

__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.old_search"

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