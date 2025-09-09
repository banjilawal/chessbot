from assurance.validators.coord import CoordValidator
from assurance.validators.name import NameValidator
from chess.common.result import SearchResult
from chess.geometry.coord import Coord
from chess.side.model import Side
from chess.token.model import Piece


class SideSearch:
    """Static search methods within a single side"""

    @staticmethod
    def by_id(piece_id: int, side: 'Side') -> SearchResult['Piece']:
        method = "SideSearch.by_id"
        """Find a piece by ID within a specific side"""

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
        """Find a piece by name within a specific side"""

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
        """Find a piece by coordinate within a specific side"""

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


