from typing import List

from assurance.validators.coord import CoordValidator
from assurance.validators.name import NameValidator
from chess.common.result import SearchResult
from chess.geometry.coord import Coord
from chess.search.side_search import SideSearch
from chess.side.model import Side
from chess.token.model import Piece


class PieceSearch:
    """Static search methods for Piece entities"""


    @staticmethod
    def by_coord(coord: Coord, sides: List['Side']) -> SearchResult['Piece']:
        """Find a piece by coordinate across all sides"""
        try:
            # Validate input
            validation = CoordValidator.validate(coord)
            if not validation.is_success():
                return SearchResult(exception=validation.exception)

            # Search all sides
            for side in sides:
                piece_result = SideSearch.by_coord(coord, side)
                if piece_result.is_success():
                    return piece_result

            return SearchResult()  # Not found anywhere

        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def by_name(piece_name: str, sides: List['Side']) -> SearchResult['Piece']:
        """Find a piece by name across all sides"""
        try:
            validation = NameValidator.validate(piece_name)
            if not validation.is_success():
                return SearchResult(exception=validation.exception)

            for side in sides:
                piece_result = SideSearch.by_name(piece_name, side)
                if piece_result.is_success():
                    return piece_result

            return SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def by_id(piece_id: int, sides: List['Side']) -> SearchResult['Piece']:
        """Find a piece by ID across all sides"""
        try:
            for side in sides:
                piece_result = SideSearch.by_id(piece_id, side)
                if piece_result.is_success():
                    return piece_result

            return SearchResult()

        except Exception as e:
            return SearchResult(exception=e)