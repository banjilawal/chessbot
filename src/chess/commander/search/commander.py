
from chess.commander import Commander, CommanderValidator
from chess.team import Team
from chess.commander.search import SearchResult
from chess.system import IdValidator

class CommanderSearch:
  """
  Static methods for entities and operations that need to old_search team Board for pieces, squares, coords, etc.
  Provides consistent old_search interface and return types across all old_search operations.
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
    `SearchResult`: The return type for all old_search operations
  """

  @staticmethod
  def for_team(team_id: int, commander: 'Commander') -> SearchResult['Team']:
    method = "CommanderSearch.for_team"
    """Find team discover by ID within team specific commander"""

    try:
      id_validation = IdValidator.validate(team_id)
      if not id_validation.is_success():
        raise id_validation.exception

      commander_validation = CommanderValidator.validate(commander)
      if not commander_validation.is_success():
        raise commander_validation.exception

      team = next((team for team in commander.teams.items if team.id == team_id), None)
      if team is not None:
        return SearchResult(payload=team)

      # returns empty old_search result
      return SearchResult()

    except Exception as e:
      return SearchResult(exception=e)


