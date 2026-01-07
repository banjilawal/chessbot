# src/chess/board_validator/board_validator.py
"""
Module: chess.board_validator.board_validator
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation 1***: No coord_stack_validator, error checking is performed in `Board` class. Using the class directly instead of
  its CRUD interfaces goes against recommended usage.

***Limitation 2***: There is no guarantee properly created `Board` objects released by the module will satisfy client
    requirements. Clients are responsible for ensuring a `BoardBuilder` product will not fail when used. Products
    from `BoardBuilder` --should-- satisfy `BoardValidator` requirements.

**Related Features**:
    Authenticating existing boards -> See BoardValidator, module[chess.board_validator.coord_stack_validator],
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

From `chess.board_validator`:
    `Board`, `NullBoard`, `BoardBuildFailedException`, `BoardSchema`

From `chess.player_agent`:
  `Player`, `PlayerAgentValidator`,

From `chess.owner`:
  `Token`

# CONTAINS:
----------
 * `Board`
"""

from typing import List

from chess.battle_space import Projection, ProjectionSearchContext
from chess.battle_space.service import ProjectionService
from chess.coord import Coord
from chess.piece import Piece
from chess.board import Board, BoardContext, BoardSearchContextValidator, BoardValidator
from chess.system import (
    Finder, SearchResult, LoggingLevelRouter, PieceSearchNameCollisionException, PieceSearchCoordCollisionException,
    PieceSearchIdCollisionException
)


class WhiteTeamProjectionFinder(Finder[ProjectionService, Projection]):
    """"""

    @classmethod
    @LoggingLevelRouter.monitor
    def search(cls, service: ProjectionService, search_context: ProjectionSearchContext) -> SearchResult[List[Projection]]:
        """"""
        method = "WhiteTeamProjectionFinder.searcher"

        service_validation = ProjectionServiceValidator.validate(service)
        if service_validation.is_failure():
            return SearchResult(exception=service_validation.exception)

        search_context_validation = BoardSearchContextValidator.validate(search_context)
        if search_context_validation.is_failure():
            return SearchResult(exception=search_context_validation.exception)

        if search_context.id is not None:
            return BoardPieceSearch._id_search(board=board, id=search_context.id)

        if search_context.name is not None:
            return BoardPieceSearch._name_search(board=board, name=search_context.name)

        if search_context.coord is not None:
            return WhiteTeamProjectionFinder._coord_search(board=board, ransom=search_context.coord)


    @classmethod
    @LoggingLevelRouter.monitor
    def _id_search(cls, board: Board, id: int) -> SearchResult[List[Piece]]:
        method = "BoardPieceFinder._id_search"
        try:
            matches = [piece for piece in board.pieces if piece.id == id]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return BoardPieceSearch._resolve_duplicate_ids(duplicates=matches, board=board)
        except Exception as e:
            return SearchResult(exception=e)


    @classmethod
    @LoggingLevelRouter.monitor
    def _name_search(cls, board: Board, name: str) -> SearchResult[List[Piece]]:
        method = "BoardPieceFinder._name_search"
        try:
            matches = [piece for piece in board.pieces if piece.name.upper == name.upper()]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return BoardPieceSearch._resolve_duplicate_names(duplicates=matches, board=board)
        except Exception as e:
            return SearchResult(exception=e)

    @classmethod
    @LoggingLevelRouter.monitor
    def _coord_search(cls, board: Board, coord: Coord) -> SearchResult[List[Piece]]:
        method = "BoardPieceFinder._coord_search"
        try:
            matches = [piece for piece in board.pieces if piece.current_position == coord]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return BoardPieceSearch._resolve_duplicate_coords(matches=matches, board=board)
        except Exception as e:
            return SearchResult(exception=e)


    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_matching_ids(cls, matches: List[Piece], board: Board) -> SearchResult[List[Piece]]:
        method = "BoardPieceFinder._resolve_matching_ids"
        target = matches.pop()
        misses = [piece for piece in matches if piece.id == target.id and (
                piece.name.upper() != target.name.upper() or piece.current_position != target.current_position
            )
        ]
        if len(misses) == 0:
            runs = len(matches) - 1
            for piece in board.pieces:
                if (
                    piece.id == target.id and
                    piece.name.upper() == target.name.upper() and
                    piece.current_position == target.current_position
                ):
                    board.pieces.remove(piece)
                    matches.remove(piece)
            return SearchResult(payload=matches)
        return SearchResult(exception=PieceSearchIdCollisionException(
                f"{method}: {PieceSearchIdCollisionException.DEFAULT_MESSAGE}"
            )
        )

    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_matching_names(cls, matches: List[Piece], board: Board) -> SearchResult[List[Piece]]:
        method = "BoardPieceFinder._resolve_matching_names"
        target = matches.pop()
        misses = [piece for piece in matches if piece.name.upper() == target.name.upper() and (
                piece.id != target.id or piece.current_position != target.current_position
            )
        ]
        if len(misses) == 0:
            runs = len(matches) - 1
            for piece in board.pieces:
                if (
                    piece.id == target.id and
                    piece.name.upper() == target.name.upper() and
                    piece.current_position == target.current_position
                ):
                    board.pieces.remove(piece)
                    matches.remove(piece)
            return SearchResult(payload=matches)
        return SearchResult(exception=PieceSearchNameCollisionException(
                f"{method}: {PieceSearchNameCollisionException.DEFAULT_MESSAGE}"
            )
        )

    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_matching_coords(cls, matches: List[Piece], board: Board) -> SearchResult[List[Piece]]:
        method = "BoardPiceSearch._resolve_matching_coords"
        target = matches.pop()
        misses = [piece for piece in matches if piece.current_position == target.current_position and (
                piece.name.upper() != target.name.upper() or piece.id != target.id
            )
        ]
        if len(misses) == 0:
            runs = len(matches) - 1
            for piece in board.pieces:
                if (
                    piece.id == target.id and
                    piece.name.upper() == target.name.upper() and
                    piece.current_position == target.current_position
                ):
                    board.pieces.remove(piece)
                    matches.remove(piece)
            return SearchResult(payload=matches)
        return SearchResult(exception=PieceSearchCoordCollisionException(
                f"{method}: {PieceSearchCoordCollisionException.DEFAULT_MESSAGE}"
            )
        )
              
          
      
      
      
    