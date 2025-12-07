# src/chess/board/searcher/piece/service.py

"""
Module: chess.board.searcher.piece.searcher
Author: Banji Lawal
Created: 2025-10-16
version: 1.0.0
"""

from typing import List

from chess.coord import Coord
from chess.piece import Piece
from chess.board import Board, BoardSearchContext, BoardSearchContextValidator, BoardValidator
from chess.system import (
    Search, SearchResult, LoggingLevelRouter, PieceSearchNameCollisionException, PieceSearchCoordCollisionException, 
    PieceSearchIdCollisionException
)


class BoardPieceSearch(Search[Board, Piece]):
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
    def search(cls, board: Board, search_context: BoardSearchContext) -> SearchResult[List[Piece]]:
        method = "BoardPieceSearch.old_search"

        board_validation = BoardValidator.validate(board)
        if board_validation.is_failure():
            return SearchResult(exception=board_validation.exception)

        search_context_validation = BoardSearchContextValidator.validate(search_context)
        if search_context_validation.is_failure():
            return SearchResult(exception=search_context_validation.exception)

        if search_context.id is not None:
            return BoardPieceSearch._id_search(board=board, id=search_context.id)

        if search_context.name is not None:
            return BoardPieceSearch._name_search(board=board, name=search_context.name)

        if search_context.current_position is not None:
            return BoardPieceSearch._coord_search(board=board, ransom=search_context.current_position)


    @classmethod
    @LoggingLevelRouter.monitor
    def _id_search(cls, board: Board, id: int) -> SearchResult[List[Piece]]:
        method = "BoardPieceSearch._id_search"
        try:
            matches = [piece for piece in board.pieces if piece.id == id]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return BoardPieceSearch._resolve_matching_ids(matches=matches, board=board)
        except Exception as ex:
            return SearchResult(exception=ex)


    @classmethod
    @LoggingLevelRouter.monitor
    def _name_search(cls, board: Board, name: str) -> SearchResult[List[Piece]]:
        method = "BoardPieceSearch._name_search"
        try:
            matches = [piece for piece in board.pieces if piece.name.upper == name.upper()]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return BoardPieceSearch._resolve_matching_names(matches=matches, board=board)
        except Exception as e:
            return SearchResult(exception=e)

    @classmethod
    @LoggingLevelRouter.monitor
    def _coord_search(cls, board: Board, coord: Coord) -> SearchResult[List[Piece]]:
        method = "BoardPieceSearch._coord_search"
        try:
            matches = [piece for piece in board.pieces if piece.current_position == coord]
            if len(matches) == 0:
                return SearchResult()
            elif len(matches) == 1:
                return SearchResult(payload=matches)
            else:
                return BoardPieceSearch._resolve_matching_coords(matches=matches, board=board)
        except Exception as e:
            return SearchResult(exception=e)


    @classmethod
    @LoggingLevelRouter.monitor
    def _resolve_matching_ids(cls, matches: List[Piece], board: Board) -> SearchResult[List[Piece]]:
        method = "BoardPieceSearch._resolve_matching_ids"
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
        method = "BoardPieceSearch._resolve_matching_names"
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
              
          
      
      
      
    