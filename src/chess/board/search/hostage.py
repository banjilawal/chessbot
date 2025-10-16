# src/chess/board/board.py
"""
Module: chess.board.board
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation 1***: No validation, error checking is performed in `Board` class. Using the class directly instead of
  its CRUD interfaces goes against recommended usage.

***Limitation 2***: There is no guarantee properly created `Board` objects released by the module will satisfy client
    requirements. Clients are responsible for ensuring a `BoardBuilder` product will not fail when used. Products
    from `BoardBuilder` --should-- satisfy `BoardValidator` requirements.

**Related Features**:
    Authenticating existing boards -> See BoardValidator, module[chess.board.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data Holding, Coordination, Performance

**Design Concepts**:
    Separating object creation from object usage.
    Keeping constructors lightweight

# PURPOSE:
---------
1. Putting all the steps and logging into one place makes modules using `Board` objects cleaner and easier to follow.

***Satisfies***: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
    `BuildResult`, `Builder`, `LoggingLevelRouter`, `ChessException`, `NullException`, `BuildFailedException`
    `IdValidator`, `NameValidator`

From `chess.board`:
    `Board`, `NullBoard`, `BoardBuildFailedException`, `BoardSchema`

From `chess.commander`:
  `Commander`, `CommanderValidator`,

From `chess.piece`:
  `Piece`

# CONTAINS:
----------
 * `Board`
"""


from typing import List

from chess.coord import Coord
from chess.piece import Piece
from chess.board import Board, PieceSearchContext, BoardValidator
from chess.system import Search, SearchResult, LoggingLevelRouter
from chess.board.search import PieceSearchContextValidator


class PieceSearch(Search):
  """
  # ROLE: Builder implementation

  # RESPONSIBILITIES:
  1. Process and validate parameters for creating `Board` instances.
  2. Create new `Board` objects if parameters meet specifications.
  2. Report errors and return `BuildResult` with error details.

  # PROVIDES:
  `BuildResult`: Return type containing the built `Board` or error information.

  # ATTRIBUTES:
  None
  """
  @classmethod
  @LoggingLevelRouter.monitor
  def search(cls, board: Board, search_context: PieceSearchContext) -> SearchResult[List[Piece]]:
      method = "DiscoverySearch.old_search"

      board_validation = BoardValidator.validate(board)
      if not board_validation.is_success():
        return SearchResult(exception=board_validation.exception)

      search_context_validation = PieceSearchContextValidator.validate(search_context)
      if not search_context_validation.is_success():
        return SearchResult(exception=search_context_validation.exception)

      if search_context.piece_id is not None:
        return PieceSearch._id_search(board=board, piece_id=search_context.piece_id)

      if search_context.name is not None:
        return PieceSearch._name_search(board=board, name=search_context.name)

      if search_context.coord is not None:
        return PieceSearch._coord_search(board=board, ransom=search_context.coord)


  @classmethod
  @LoggingLevelRouter.monitor
  def _name_search(cls, board: Board, name: str) -> SearchResult[List[Piece]]:
      """
      Does not guarantee uniqueness returns the first item which matches the given name.
      """
      method = "DiscoverySearch._name_search"

      try:
          matches = [piece for piece in board.pieces if piece.name.upper == name.upper()]

          if len(matches) > 1:
              return SearchResult(exception=SearchNameCollisionException(
                  f"{method}: {SearchNameCollisionException.DEFAULT_MESSAGE}"
                )
              )
          if len(matches) == 0:
              return SearchResult()

          return SearchResult(payload=matches)
      except Exeception as e:
        return SearchResult(exception=e)


  @classmethod
  @LoggingLevelRouter.monitor
  def _coord_search(cls, board: Board, coord: Coord) -> SearchResult[List[Piece]]:
      """
      Does not guarantee uniqueness returns the first item which matches the given name.
      """
      method = "DiscoverySearch._name_search"

      try:
          matches = [piece for piece in board.pieces if piece.current_position == coord]

          if len(matches) > 1:
              return SearchResult(exception=BoardPieceCollisionException(
                  f"{method}: {SearchCoordCollisionException.DEFAULT_MESSAGE}"
                )
              )
          if len(matches) == 0:
              return SearchResult()

          return SearchResult(payload=matches)
      except Exeception as e:
          return SearchResult(exception=e)


  @classmethod
  @LoggingLevelRouter.monitor
  def _id_search(cls, board: Board, piece_id: int) -> SearchResult[List[Piece]]:
      """
      Does not guarantee uniqueness returns the first item which matches the given name.
      """
      method = "DiscoverySearch._name_search"

      try:
          matches = [piece for piece in board.pieces if piece.id== piece_id]

          if len(matches) > 1:
              return SearchResult(exception=BoardPieceCollisionException(
                  f"{method}: {SearchCIdCollisionException.DEFAULT_MESSAGE}"
                )
              )
          if len(matches) == 0:
              return SearchResult()

          return SearchResult(payload=matches)
      except Exeception as e:
          return SearchResult(exception=e)