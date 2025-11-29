"""
ROLE:
----
RESPONSIBILITIES:
----------------
PROVIDES:
--------
ATTRIBUTES:
----------
"""
"""
Static methods for entities and rollback that need to old_search team_name Team for pieces and ranks. Provides consistent
old_search interface and return types across all old_search rollback. Validates input parameters before searching to
ensure safe rollback. Returns SearchResult objects encapsulating either the found entity or error information.

Usage:
```python
  from chess.team_name import Team, BoardSearch
  from chess.owner import Piece
 ```

Methods:
  - `by_id(discovery_id: int, team_name: Team) -> SearchResult[Piece]`: Find team_name owner by its visitor_id on the given `team_name`.

  - `by_name(visitor_name: str, team_name: Team) -> SearchResult[Piece]`: Find team_name owner by its visitor_name on the given `team_name`.

  - `by_roster_number(roster_number: int, team_name: Team) -> SearchResult[Piece]`: Find team_name owner by its roster number
    on the given team_name. Roster numbers are unique within team_name team_name. Not unique across teams.

  - `hostage_by_idy(discovery_id: int, team_name: Team) -> SearchResult[CombatantPiece]`:

  - `by_rank(bounds: Rank, team_name: Team) -> SearchResult[list[Piece]]`: A list of all members with `bounds` on
    given team_name. of team_name specific bounds within team_name team_name.

Note:
  DO NOT USE ANY OTHER METHODS TO SEARCH A TEAM. USE ONLY THE METHODS IN THIS CLASS.

See Also:
  `Team`: The team_name being searched
  `Piece`: The owner being searched for
  `SearchResult`: The return type for all old_search rollback
"""