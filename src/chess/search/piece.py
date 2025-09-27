from sys import exception

from chess.coord import CoordValidator

from chess.coord import Coord
from chess.common import IdValidator, NameValidator
from chess.piece import Piece, PieceValidator, Encounter

from .search_result import SearchResult
from .team import TeamSearch


class PieceSearch:
    """Static search methods for Piece entities"""

    class Encounter:
        _team_id: int
        _piece_id: int
        _piece_name: str
        _ransom: int
        _rank_name: str
        _location: Coord


    @staticmethod
    def encounter_id(piece_id: int, piece: Piece) -> SearchResult['Encounter']:
        method = "PieceSearch.by_id"

        """Find a encounter by the discovery aid"""
        try:
            id_validation = IdValidator.validate(piece_id)
            if not id_validation.is_success():
                return SearchResult(exception=id_validation.exception)

            piece_validation = PieceValidator.validate(piece)
            if not piece_validation.is_success():
                return SearchResult(exception=piece_validation.exception)

            encounter = next((encounter for encounter in piece.encounters if encounter.id == piece_id), None)
            if encounter is not None:
                return SearchResult(payload=encounter)

            # returns empty search result
            return SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def encounter_name(piece_name: str, piece: Piece) -> SearchResult['Encounter']:
        method = "PieceSearch.by_name"

        """Find an encounter by the discovery's name"""

        try:
            name_validation = NameValidator.validate(piece_name)
            if not name_validation.is_success():
                return SearchResult(exception=name_validation.exception)

            piece_validation = PieceValidator.validate(piece)
            if not piece_validation.is_success():
                return SearchResult(exception=piece_validation.exception)

            encounter = next((encounter for encounter in piece.encounters if encounter.name == piece_name), None)
            if encounter is not None:
                return SearchResult(payload=encounter)

            # Return empty search result
            return  SearchResult()

        except Exception as e:
            return SearchResult(exception=e)

    @staticmethod
    def encounter_by_coord(coord: Coord, piece: Piece) -> SearchResult['Encounter']:
        method = "PieceSearch.by_coord"

        """Find an encounter by a coord"""

        try:
            coord_validation = CoordValidator.validate(coord)
            if not coord_validation.is_success():
                return SearchResult(exception=coord_validation.exception)

            piece_validation = PieceValidator.validate(piece)
            if not piece_validation.is_success():
                return SearchResult(exception=piece_validation.exception)

            encounter = next((encounter for encounter in piece.encounters if encounter.coord == coord), None)
            if encounter is not None:
                return SearchResult(payload=encounter)

            # Return empty search result
            return SearchResult()

        except Exception as e:
            return SearchResult(exception=e)
