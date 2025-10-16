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

From `chess.square`:
  `Square`

# CONTAINS:
----------
 * `Board`
"""

from typing import List


from chess.coord import Coord
from chess.square import Square

from chess.board import Board, BoardSearchContext, BoardSearchContextValidator
from chess.system import (
    Search, SearchResult, LoggingLevelRouter, SquareSearchNameCollisionException, SquareSearchCoordCollisionException, 
    SquareSearchIdCollisionException
)



class BoardSquareSearch(Search[Board, Square]):
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
    def search(cls, board: Board, search_context: BoardSearchContext) -> SearchResult[List[Square]]:
        method = "BoardPieceSearch.old_search"

        # board_validation = BoardValidator.validate(board)
        # if not board_validation.is_success():
        #     return SearchResult(exception=board_validation.exception)

        search_context_validation = BoardSearchContextValidator.validate(search_context)
        if not search_context_validation.is_success():
            return SearchResult(exception=search_context_validation.exception)

        if search_context.id is not None:
            return BoardSquareSearch._id_search(board=board, id=search_context.id)

        if search_context.name is not None:
            return BoardSquareSearch._name_search(board=board, name=search_context.name)

        if search_context.coord is not None:
            return BoardSquareSearch._coord_search(board=board, ransom=search_context.coord)


    @classmethod
    @LoggingLevelRouter.monitor
    def _id_search(cls, board: Board, id: int) -> SearchResult[List[Square]]:
        method = "BoardPieceSearch._id_search"
        try:
            matches = [square for square in board.squares if square.id == id]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return BoardSquareSearch._resolve_matching_ids(matches=matches, board=board)
        except Exception as e:
            return SearchResult(exception=e)


    @classmethod
    @LoggingLevelRouter.monitor
    def _name_search(cls, board: Board, name: str) -> SearchResult[List[Square]]:
        method = "BoardPieceSearch._name_search"
        try:
            matches = [square for square in board.squares if square.name.upper == name.upper()]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return BoardSquareSearch._resolve_matching_names(matches=matches, board=board)
        except Exception as e:
            return SearchResult(exception=e)


    @classmethod
    @LoggingLevelRouter.monitor
    def _coord_search(cls, board: Board, coord: Coord) -> SearchResult[List[Square]]:
        method = "BoardPieceSearch._coord_search"
        try:
            matches = [square for square in board.squares if square.coord == coord]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return BoardSquareSearch._resolve_matching_coords(matches=matches, board=board)
        except Exception as e:
            return SearchResult(exception=e)


    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_matching_ids(cls, matches: List[Square], board: Board) -> SearchResult[List[Square]]:
        method = "BoardPieceSearch._resolve_matching_ids"
        target = matches.pop()
        misses = [square for square in matches if square.id == target.id and (
                square.name.upper() != target.name.upper() or square.coord != target.coord
            )
        ]
        if len(misses) == 0:
            runs = len(matches) - 1
            for square in board.squares:
                if (
                    square.id == target.id and
                    square.name.upper() == target.name.upper() and
                    square.coord == target.coord
                ):
                    board.squares.remove(square)
                    matches.remove(square)
            return SearchResult(payload=matches)
        return SearchResult(exception=SquareSearchIdCollisionException(
                f"{method}: {SquareSearchIdCollisionException.DEFAULT_MESSAGE}"
            )
        )

    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_matching_names(cls, matches: List[Square], board: Board) -> SearchResult[List[Square]]:
        method = "BoardPieceSearch._resolve_matching_names"
        target = matches.pop()
        misses = [square for square in matches if square.name.upper() == target.name.upper() and (
                square.id != target.id or square.coord != target.coord
            )
        ]
        if len(misses) == 0:
            runs = len(matches) - 1
            for square in board.squares:
                if (
                    square.id == target.id and
                    square.name.upper() == target.name.upper() and
                    square.coord == target.coord
                ):
                    board.squares.remove(square)
                    matches.remove(square)
            return SearchResult(payload=matches)
        return SearchResult(exception=SquareSearchIdCollisionException(
                f"{method}: {SquareSearchIdCollisionException.DEFAULT_MESSAGE}"
            )
        )

    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_matching_coords(cls, matches: List[Square], board: Board) -> SearchResult[List[Square]]:
        method = "BoardPieceSearch._resolve_matching_coords"
        target = matches.pop()
        misses = [square for square in matches if square.coord == target.coord and (
                square.name.upper() != target.name.upper() or square.id != target.id
            )
        ]
        if len(misses) == 0:
            runs = len(matches) - 1
            for square in board.squares:
                if (
                    square.id == target.id and
                    square.name.upper() == target.name.upper() and
                    square.coord == target.coord
                ):
                    board.squares.remove(square)
                    matches.remove(square)
            return SearchResult(payload=matches)
        return SearchResult(exception=SquareSearchIdCollisionException(
                f"{method}: {SquareSearchIdCollisionException.DEFAULT_MESSAGE}"
            )
        )
              
          
      
      
      
    