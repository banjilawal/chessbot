
from chess.commander import Commander, CommanderValidator
from chess.piece.piece import Piece
from chess.search import SearchResult
from assurance import IdValidator, NameValidator

class CommanderSearch:
    """Static search methods within a single commander"""

    @staticmethod
    def for_team(team_id: int, commander: 'Commander') -> SearchResult['Piece']:
        method = "CommanderSearch.for_team"
        """Find a piece by ID within a specific commander"""

        try:
            id_validation = IdValidator.validate(team_id)
            if not id_validation.is_success():
                raise id_validation.exception

            commander_validation = CommanderValidator.validate(commander)
            if not commander_validation.is_success():
                raise commander_validation.exception

            team = next((team for team in commander.teams if team.id == team_id), None)
            if team is not None:
                return SearchResult(payload=team)

            # returns empty search result
            return SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def by_name(name: str, commander: 'Commander') -> SearchResult['Piece']:
        method = "CommanderSearch.by_coord"
        """Find a piece by name within a specific commander"""

        try:
            validation = NameValidator.validate(name)
            if not validation.is_success():
                return  SearchResult(exception=validation.exception)

            piece = next((member for member in commander.roster if member.name.upper() == name.upper()), None)
            if piece is not None:
                return SearchResult(payload=piece)

            # returns empty search result
            return SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def by_roster_number(roster_number: int, commander: Commander) -> SearchResult['Piece']:
        method = f"CommanderSearch.by_roster"

        """
        Find a piece with the `roster_number`. 

        Args:
           `roster_number` (`int`): There are 16 chess pieces per commander. jersey_range = [0,15]

        Returns:
            `SearchResult`: `Piece` if a match is found other wise `None`

        Raises:
             `IdValidationException`
        """

        try:
            validation = IdValidator.validate(roster_number)
            if not validation.is_success():
                raise validation.exception

            piece = next((member for member in commander.roster if member.roster_number == roster_number), None)
            if piece is not None:
                return SearchResult(payload=piece)

            # returns empty search result
            return SearchResult()

        except Exception as e:
            return SearchResult(exception=e)


