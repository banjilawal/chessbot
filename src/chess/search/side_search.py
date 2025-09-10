from chess.geometry.validator.coord_validator import CoordValidator
from assurance.validators.name import NameValidator

from chess.geometry.coord import Coord
from chess.side.team import Side
from chess.piece.piece import Piece

from .search_result import SearchResult


class SideSearch:
    """Static search methods within a single team"""

    @staticmethod
    def by_id(piece_id: int, side: 'Side') -> SearchResult['Piece']:
        method = "SideSearch.by_id"
        """Find a piece by ID within a specific team"""

        try:
            for piece in side.roster:
                if piece.id == piece_id:
                    return SearchResult(payload=piece)
            return SearchResult()
        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def by_name(piece_name: str, side: 'Side') -> SearchResult['Piece']:
        "SideSearch.by_name"
        """Find a piece by name within a specific team"""

        try:
            validation = NameValidator.validate(piece_name)
            if not validation.is_success():
                return  SearchResult(exception=validation.exception)

            for piece in side.roster:
                if piece.name.upper() == piece_name.upper():
                    return SearchResult(payload=piece)
            return SearchResult()
        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def by_coord(coord: Coord, side: 'Side') -> SearchResult['Piece']:
        method = "SideSearch.by_coord"
        """Find a piece by coordinate within a specific team"""

        try:
            validation = CoordValidator.validate(coord)
            if not validation.is_success():
                return  SearchResult(exception=validation.exception)

            piece = next((p for p in side.roster if p.current_position == coord), None)
            if piece is not None:
                return SearchResult(payload=piece)

            return SearchResult()
        except Exception as e:
            return SearchResult(exception=e)


