
from chess.team import Team, TeamValidator
from chess.piece.piece import Piece
from chess.search import SearchResult
from chess.rank import Rank, RankValidator
from chess.common import IdValidator, NameValidator

class TeamSearch:
    """
    Static methods for entities and operations that need to search a Team for pieces and ranks. Provides consistent
    search interface and return types across all search operations. Validates input parameters before searching to
    ensure safe operations. Returns SearchResult objects encapsulating either the found entity or error information.

    Usage:
    ```python
        from chess.team import Team, TeamSearch
        from chess.piece import Piece
     ```
     
    Methods:
        - `by_id(discovery_id: int, team: Team) -> SearchResult[Piece]`: Find a piece by its id on the given `team`.
        
        - `by_name(name: str, team: Team) -> SearchResult[Piece]`: Find a piece by its name on the given `team`.
        
        - `by_roster_number(roster_number: int, team: Team) -> SearchResult[Piece]`: Find a piece by its roster number
            on the given team. Roster numbers are unique within a team. Not unique across teams.
            
        - `hostage_by_idy(discovery_id: int, team: Team) -> SearchResult[CombatantPiece]`:
            
        - `by_rank(rank: Rank, team: Team) -> SearchResult[list[Piece]]`: A list of all members with `rank` on 
            given team. of a specific rank within a team.

    Note:
        DO NOT USE ANY OTHER METHODS TO SEARCH A TEAM. USE ONLY THE METHODS IN THIS CLASS.

    See Also:
        `Team`: The team being searched
        `Piece`: The piece being searched for
        `SearchResult`: The return type for all search operations
    """

    @staticmethod
    def by_id(piece_id: int, team: 'Team') -> SearchResult['Piece']:
        """
        Find a piece within the given `team` that whose `id` matches the search target. Ids are unique within the system.
        TeamSearch.by_id is the recommended way to find a piece by id within a specific team.
        Args:
          `id` (`str`): A valid id
          `team` (`Team`): a valid team

        Returns:
              SearchResult[Team]: A `SearchResult` containing either:
                  - On success: The validated Team instance in the payload
                  - On not found: An empty `SearchResult` (payload is None, exception is None)
                  - On failure: Error information and exception details
        Raises:
            `InvalidIdException`
            `InvalidTeamException`
        """
        method = "TeamSearch.by_id"

        try:
            id_validation = IdValidator.validate(piece_id)
            if not id_validation.is_success():
                return SearchResult(exception=id_validation.exception)

            team_validation = TeamValidator.validate(team)
            if not team_validation.is_success():
                return SearchResult(exception=team_validation.exception)

            piece = next((member for member in team.roster if member.id == id), None)
            if piece is not None:
                return SearchResult(payload=piece)

            # returns empty search result
            return SearchResult()

        # Catch any unexpected exceptions and put them in the SearchResult
        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def by_name(name: str, team: 'Team') -> SearchResult['Piece']:
        """
        Find a piece within the given `team` that whose name matches the search target. Names are unique within
        a `Game` instance but not across games.

        Args:
          `name` (`str`): A valid name in the system
          `team` (`Team`): a valid team

        Returns:
              SearchResult[Team]: A `SearchResult` containing either:
                  - On success: The validated Team instance in the payload
                  - On not found: An empty `SearchResult` (payload is None, exception is None)
                  - On failure: Error information and exception details
        Raises:
            `InvalidNameException`
            `InvalidTeamException`
        """
        method = "TeamSearch.by_roster"

        try:
            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                return  SearchResult(exception=name_validation.exception)

            team_validation = TeamValidator.validate(team)
            if not team_validation.is_success():
                return SearchResult(exception=team_validation.exception)

            piece = next((member for member in team.roster if member.name.upper() == name.upper()), None)
            if piece is not None:
                return SearchResult(payload=piece)

            # returns empty search result
            return SearchResult()

        # Catch any unexpected exceptions and put them in the SearchResult
        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def by_roster_number(roster_number: int, team: Team) -> SearchResult['Piece']:
        """
        Find a piece with the `roster_number`.  Roster numbers are unique within a team. Not unique across teams.
        There are 16 chess pieces per team. jersey_range = [0,15]

        Args:
          `roster_number` (`int`): Between 0 and 15 inclusive
          `team` (`Team`): a valid team

        Returns:
              SearchResult[Team]: A `SearchResult` containing either:
                  - On success: The validated Team instance in the payload
                  - On not found: An empty `SearchResult` (payload is None, exception is None)
                  - On failure: Error information and exception details
        Raises:
            `IdValidationException`
            `InvalidTeamException`
        """
        method = "TeamSearch.by_roster"

        try:
            roster_number__validation = IdValidator.validate(roster_number)
            if not roster_number__validation.is_success():
                return SearchResult(exception=roster_number__validation.exception)

            team_validation = TeamValidator.validate(team)
            if not team_validation.is_success():
                return SearchResult(exception=team_validation.exception)


            piece = next(
                (member for member in team.roster if member.roster_number == roster_number),
                None
            )
            if piece is not None:
                return SearchResult(payload=piece)

            # returns empty search result
            return SearchResult()

        # Catch any unexpected exceptions and put them in the SearchResult
        except Exception as e:
            return SearchResult(exception=e)

    @staticmethod
    def hostage_id(hostage_id: int, team: 'Team') -> SearchResult['Piece']:
        """
        Find a piece within the given `team` that whose name matches the search target. Names are unique within
        a `Game` instance but not across games.

        Args:
          `hostage_id` (`id`): The id of the hostage piece
          `team` (`Team`): a valid team

        Returns:
              SearchResult[Team]: A `SearchResult` containing either:
                  - On success: The validated Team instance in the payload
                  - On not found: An empty `SearchResult` (payload is None, exception is None)
                  - On failure: Error information and exception details
        Raises:
            `InvalidNameException`
            `InvalidTeamException`
        """
        method = "TeamSearch.bostage_id"

        try:
            id_validation = IdValidator.validate(hostage_id)
            if not id_validation.is_success():
                return SearchResult(exception=id_validation.exception)

            team_validation = TeamValidator.validate(team)
            if not team_validation.is_success():
                return SearchResult(exception=team_validation.exception)

            enemy = next((hostage for hostage in team.hostages if hostage.id == hostage_id), None)
            if enemy is not None:
                return SearchResult(payload=enemy)

            # returns empty search result
            return SearchResult()

        # Catch any unexpected exceptions and put them in the SearchResult
        except Exception as e:
            return SearchResult(exception=e)


    @staticmethod
    def by_rank(rank: Rank, team: 'Team') -> SearchResult[list['Piece']]:
        method = "TeamSearch.by_rank"
        """Find a piece by ID within a specific team"""

        try:
            validation = RankValidator.validate(rank)
            if not validation.is_success():
                raise validation.exception

            matches = [piece for piece in team.roster if piece.rank == rank]
            return SearchResult(payload=matches)

        # Catch any unexpected exceptions and put them in the SearchResult
        except Exception as e:
            return SearchResult(exception=e)


