
from chess.team import Team
from chess.piece.piece import Piece
from chess.search import SearchResult
from assurance import IdValidator, NameValidator

class TeamSearch:
    """Static search methods within a single team"""

    @staticmethod
    def by_id(piece_id: int, team: 'Team') -> SearchResult['Piece']:
        method = "TeamSearch.by_id"
        """Find a piece by ID within a specific team"""

        try:
            validation = IdValidator.validate(piece_id)
            if not validation.is_success():
                raise validation.exception

            piece = next((member for member in team.roster if member.id == id), None)
            if piece is not None:
                return SearchResult(payload=piece)

            # returns empty search result
            return SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def by_name(name: str, team: 'Team') -> SearchResult['Piece']:
        method = "TeamSearch.by_coord"
        """Find a piece by name within a specific team"""

        try:
            validation = NameValidator.validate(name)
            if not validation.is_success():
                return  SearchResult(exception=validation.exception)

            piece = next((member for member in team.roster if member.name.upper() == name.upper()), None)
            if piece is not None:
                return SearchResult(payload=piece)

            # returns empty search result
            return SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def by_roster_number(roster_number: int, team: Team) -> SearchResult['Piece']:
        method = f"TeamSearch.by_roster"

        """
        Find a piece with the `roster_number`. 

        Args:
           `roster_number` (`int`): There are 16 chess pieces per team. jersey_range = [0,15]

        Returns:
            `SearchResult`: `Piece` if a match is found other wise `None`

        Raises:
             `IdValidationException`
        """

        try:
            validation = IdValidator.validate(roster_number)
            if not validation.is_success():
                raise validation.exception

            piece = next((member for member in team.roster if member.roster_number == roster_number), None)
            if piece is not None:
                return SearchResult(payload=piece)

            # returns empty search result
            return SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


