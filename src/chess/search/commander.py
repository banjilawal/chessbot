
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


