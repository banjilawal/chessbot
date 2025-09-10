from chess.geometry.validator.coord_validator import CoordValidator
from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator
from chess.board.board import Board
from chess.square import Square
from chess.result import SearchResult
from chess.geometry.coord import Coord


class SquareSearch:
    """Static search methods for Square entities"""

    @staticmethod
    def by_id(square_id: int, board: 'Board') -> SearchResult['Square']:
        method = "SquareSearch.by_id"
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



    @staticmethod
    def by_coord(coord: Coord, board: 'Board') ->  SearchResult['Square']:
        method = "SquareSearch.by_coord"
        """Find a square by coordinate"""

        try:
            validation = CoordValidator.validate(coord)
            if not validation.is_success():
                return  SearchResult(exception=validation.exception)

            square = next((s for s in board.squares if s.coord == coord), None)
            if square:
                return  SearchResult(payload=square)
            return  SearchResult()

        except Exception as e:
            return  SearchResult(exception=e)


    @staticmethod
    def by_name(name: str, board: 'Board') ->  SearchResult['Square']:
        method = "SquareSearch.by_name"
        """Find a square by name"""
        
        try:
            validation = NameValidator.validate(name)
            if not validation.is_success():
                return  SearchResult(exception=validation.exception)

            square = next((s for s in board.squares if s.name.upper() == name.upper()), None)
            if square is not None:
                return SearchResult(payload=square)
            return  SearchResult()

        except Exception as e:
            return  SearchResult(exception=e)


