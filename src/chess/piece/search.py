# src/chess/piece/piece.py
"""
Module: chess.piece.piece
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation 1***: No validation, error checking is performed in `Piece` class. Using the class directly instead of
  its CRUD interfaces goes against recommended usage.

***Limitation 2***: There is no guarantee properly created `Piece` objects released by the module will satisfy client
    requirements. Clients are responsible for ensuring a `PieceBuilder` product will not fail when used. Products
    from `PieceBuilder` --should-- satisfy `PieceValidator` requirements.

**Related Features**:
    Authenticating existing pieces -> See PieceValidator, module[chess.piece.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data Holding, Coordination, Performance

**Design Concepts**:
    Separating object creation from object usage.
    Keeping constructors lightweight

# PURPOSE:
---------
1. Putting all the steps and logging into one place makes modules using `Piece` objects cleaner and easier to follow.

***Satisfies***: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
    `BuildResult`, `Builder`, `LoggingLevelRouter`, `ChessException`, `NullException`, `BuildFailedException`
    `IdValidator`, `NameValidator`

From `chess.piece`:
    `Piece`, `NullPiece`, `PieceBuildFailedException`, `PieceSchema`

From `chess.commander`:
  `Commander`, `CommanderValidator`,

From `chess.piece`:
  `Piece`

# CONTAINS:
----------
 * `Piece`
"""


from typing import List

from chess.piece import Piece, PieceValidator, Discovery
from chess.piece import Piece, PieceSearchContext, PieceValidator
from chess.rank import Rank
from chess.system import Search, SearchResult
from chess.piece.search import PieceSearchContextValidator


class DiscoverySearch(Search):
  """
  # ROLE: Builder implementation

  # RESPONSIBILITIES:
  1. Process and validate parameters for creating `Piece` instances.
  2. Create new `Piece` objects if parameters meet specifications.
  2. Report errors and return `BuildResult` with error details.

  # PROVIDES:
  `BuildResult`: Return type containing the built `Piece` or error information.

  # ATTRIBUTES:
  None
  """
  @classmethod
  def search(cls, piece: Piece, search_context: PieceSearchContext) -> SearchResult[List[Discovery]]:
      method = "DiscoverySearch.search"

      piece_validation = PieceValidator.validate(piece)
      if not piece_validation.is_success():
        return SearchResult(exception=piece_validation.exception)

      search_context_validation = PieceSearchContextValidator.validate(search_context)
      if not search_context_validation.is_success():
        return SearchResult(exception=search_context_validation.exception)

      if search_context.name is not None:
        return DiscoverySearch._name_search(piece=piece, name=search_context.name)

      if search_context.rank is not None:
        return DiscoverySearch._rank_filter(piece=piece, rank=search_context.rank)

      if search_context.ransom is not None:
        return DiscoverySearch._ransom_filter(piece=piece, ransom=search_context.ransom)

      if search_context.piece_id is not None:
        return DiscoverySearch._id_search(piece=piece, piece_id=search_context.piece_id)

      if search_context.roster_number is not None:
        return DiscoverySearch. _roster_number_search(piece=piece, roster_number=search_context.roster_number)

  @classmethod
  def _name_search(cls, piece: Piece, name: str) -> SearchResult[List[Piece]]:
      """
      Does not guarantee uniqueness returns the first item which matches the given name.
      """
      method = "DiscoverySearch._name_search"

      prisoner = next((discovery for discovery in piece.discoveries if discovery.name.upper() == name.upper()), None)
      if prisoner is not None:
          return SearchResult(payload=List[prisoner])

      # returns empty old_search result if no match ws found
      return SearchResult()

  @classmethod
  def _rank_filter(cls, piece: Piece, rank: Rank) -> SearchResult[List[Discovery]]:
      matches = [discovery for discovery in piece.discoveries if discovery.rank == rank]
      return SearchResult(payload=matches)

  @classmethod
  def _ransom_filter(cls, piece: Piece, ransom: int) -> SearchResult[List[Discovery]]:
      matches = [discovery for discovery in piece.discoveries if discovery.rank.ransom == ransom]
      return SearchResult(payload=matches)

  @classmethod
  def _id_search(cls, piece: Piece, piece_id: int) -> SearchResult[List[Discovery]]:
      """
      IDs should be unique. Faster old_search would return the first match. An easy
      integrity check finds all the items with the same id. If there is more than
      one raise piece `DuplicateUniqueIdException`.

      Performance Impact:
      The set of discoveries will never exceed 15 so this is not going to be piece really
      burdensome old_search.
      """
      method = "DiscoverySearch._id_search"

      hit = next((discovery for discovery in piece.discoveries if discovery.id == piece_id), None)
      if hit is not None:
          return SearchResult(payload=List[hit])

      # returns empty old_search result if no match ws found
      return SearchResult()