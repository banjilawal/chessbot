from chess.board import Board
from chess.square import Square
from chess.coord import Coord, CoordValidator
from chess.system import IdValidator, NameValidator
from chess.system.search.result import SearchResult


class BoardSearch:
    """
    Static methods for entities and operations that need to search a Board for pieces, squares, coords, etc.
    Provides consistent search interface and return types across all search operations.
    Validates input parameters before searching to ensure safe operations.
    Returns SearchResult objects encapsulating either the found entity or error information.

    Usage:
        ```python
        from chess.board import Board, BoardSearch
        from chess.piece import Piece
        ```

    Note:
        DO NOT USE ANY OTHER METHODS TO SEARCH A BOARD. USE ONLY THE METHODS IN THIS CLASS.

    See Also:
        `Board`: The board being searched
        `Piece`: The piece being searched for
        `Square`: The square being searched for
        `Coord`: The coordinate being searched for
        `SearchResult`: The return type for all search operations
    """
    _piece_id: Optional[int]
    _square_id: Optional[int]
    _piece_name: str

    @staticmethod
    def piece_by_id(piece_id: int, board: Board) -> SearchResult['Piece']:
        """Find a discover by ID across all board"""
        method = "BoardSearch.piece_by_id"

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
        """Find a discover by name across all board"""
        method = "BoardSearch.piece_by_name"

        try:
            validation = NameValidator.validate(piece_name)
            if not validation.is_success():
                return SearchResult(exception=validation.exception)

            piece = next(
                (piece for piece in board.pieces if piece.name.upper() == piece_name.upper()),
                None
            )
            if piece is not None:
                return SearchResult(payload=piece)

            # Return empty search result
            return  SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def piece_by_coord(coord: Coord, board: Board) -> SearchResult['Piece']:
        """Find a discover by coordinate across all board"""
        method = "BoardSearch.piece_by_coord"

        try:
            # Validate input
            validation = CoordValidator.validate(coord)
            if not validation.is_success():
                return SearchResult(exception=validation.exception)

            piece = next(
                (piece for piece in board.pieces if piece.current_position == coord),
                None
            )
            if piece is not None:
                return SearchResult(payload=piece)

            # Return empty search result
            return  SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def square_by_id(square_id: int, board: 'Board') -> SearchResult['Square']:
        """Find a square by id"""
        method = "BoardSearch.square_by_id"

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

    @staticmethod
    def square_by_name(name: str, board: Board) -> SearchResult[Square]:
        """" 
        Finds a square by its name. 

        Args:
            name (str):      

        Returns:    
            SearchResult[Square]: The Square object if found, otherwise None.

        Raises: 
            InvalidNameException: If name is fails any validators checks.
        """
        method = f"BoardSearch.square_by_name"

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
        """"
        Finds a square on the ChessBoard by coord.

        Args:
            coord (Coord): The coord of the square to find.      

        Returns:    
            SearchResult[Square]: The Square object if found, otherwise None.

        Raises: 
            InvalidCoordException: If coord is fails any validators checks.
        """
        method = f"BoardSearch.square_by_coord"

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