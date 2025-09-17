from sys import exception

from chess.coord import CoordValidator

from chess.board import Board
from chess.square import Square, SquareValidator
from chess.coord import Coord, CoordValidator
from chess.common import IdValidator, NameValidator
from .query_result import SearchResult
from .team import TeamSearch


class BoardSearch:
    """Static search methods for Piece entities"""


    @staticmethod
    def piece_by_id(piece_id: int, board: Board) -> SearchResult['Piece']:
        """Find a piece by ID across all board"""
        try:
            id_validation= IdValidator.validate(piece_id)
            if not id_validation.is_success():
                return SearchResult(exception=id_validation.exception)

            piece = next((piece for piece in board.pieces if piece.id == piece_id), None)
            if piece is not None:
                return SearchResult(payload=piece)

            # Return empty search result
            return  SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def piece_by_name(piece_name: str, board: Board) -> SearchResult['Piece']:
        """Find a piece by name across all board"""
        try:
            validation = NameValidator.validate(piece_name)
            if not validation.is_success():
                return SearchResult(exception=validation.exception)

            piece = next((piece for piece in board.pieces if piece.id == piece_id), None)
            if piece is not None:
                return SearchResult(payload=piece)

            # Return empty search result
            return  SearchResult()


        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def piece_by_coord(coord: Coord, board: Board) -> SearchResult['Piece']:
        """Find a piece by coordinate across all board"""
        try:
            # Validate input
            validation = CoordValidator.validate(coord)
            if not validation.is_success():
                return SearchResult(exception=validation.exception)

            piece = next((piece for piece in board.pieces if piece.current_position == coord), None)
            if piece is not None:
                return SearchResult(payload=piece)

            # Return empty search result
            return  SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def square_by_id(square_id: int, board: 'Board') -> SearchResult['Square']:
        method = "BoardSearch.square_by_id"
        """Find a square by id"""

        try:
            validation = IdValidator.validate(square_id)
            if not validation.is_success():
                return SearchResult(exception=validation.exception)

            square = next((s for s in board.squares if s.id == square_id), None)
            if square is not None:
                return SearchResult(payload=square)
            return SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


    def square_by_name(self, name: str, board: Board) -> Result[Square]:
        method = f"BoardSearch.square_by_name"

        """" 
        Finds a square by its name. 

        Args:
            name (str):      

        Returns:    
            SearchResult[Square]: The Square object if found, otherwise None.

        Raises: 
            NameValidationException: If name is fails any validators checks.
        """

        try:
            validation = NameValidator.validate(name)
            if not validation.is_success():
                return  SearchResult(exception=validation.exception)

            square = next((s for s in board.squares if s.name.upper() == name.upper()), None)
            if square is not None:
                return SearchResult(payload=square)

            # returns empty search result
            return  SearchResult()

        except Exception as e:
            return  SearchResult(exception=e)


    @staticmethod
    def square_by_coord(coord: Coord, board: 'Board') ->  SearchResult['Square']:
        method = f"BoardSearch.square_by_coord"

        """" 
        Finds a square on the ChessBoard by coord.

        Args:
            coord (Coord): The coord of the square to find.      

        Returns:    
            SearchResult[Square]: The Square object if found, otherwise None.

        Raises: 
            CoordValidationException: If coord is fails any validators checks.
        """

        try:
            validation = CoordValidator.validate(coord)
            if not validation.is_success():
                return  SearchResult(exception=validation.exception)

            square = next((s for s in board.squares if s.coord == coord), None)
            if square:
                return  SearchResult(payload=square)

            # Return empty search result
            return  SearchResult()

        except Exception as e:
            return  SearchResult(exception=e)