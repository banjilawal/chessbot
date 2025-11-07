# src/chess/team/team.py
"""
Module: chess.team.team
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation 1***: No validator, error checking is performed in `Team` class. Using the class directly instead of
  its CRUD interfaces goes against recommended usage.

***Limitation 2***: There is no guarantee properly created `Team` objects released by the module will satisfy client
    requirements. Clients are responsible for ensuring a `TeamBuilder` product will not fail when used. Products
    from `TeamBuilder` --should-- satisfy `TeamValidator` requirements.

**Related Features**:
    Authenticating existing teams -> See TeamValidator, module[chess.team.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data Holding, Coordination, Performance

**Design Concepts**:
    Separating object creation from object usage.
    Keeping constructors lightweight

# PURPOSE:
---------
1. Putting all the steps and logging into one place makes modules using `Team` objects cleaner and easier to follow.

***Satisfies***: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
    `BuildResult`, `Builder`, `LoggingLevelRouter`, `ChessException`, `NullException`, `BuildFailedException`
    `IdValidator`, `NameValidator`

From `chess.team`:
    `Team`, `NullTeam`, `TeamBuildFailedException`, `TeamSchema`

From `chess.commander`:
  `Commander`, `CommanderValidator`,

From `chess.owner`:
  `Piece`

# CONTAINS:
----------
 * `Team`
"""

from typing import List

from chess.team import Team, TeamValidator
from chess.piece.model.piece import Piece
from chess.commander.search import SearchResult
from chess.system import SearchContext
from chess.team.search import TeamHostageSearch, TeamRosterSearch, PieceCollection


class TeamSearch(Piece):
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
  Static methods for entities and operations that need to old_search team Team for pieces and ranks. Provides consistent
  old_search interface and return types across all old_search operations. Validates input parameters before searching to
  ensure safe operations. Returns SearchResult objects encapsulating either the found entity or error information.

  Usage:
  ```python
    from chess.team import Team, BoardSearch
    from chess.owner import Piece
   ```
   
  Methods:
    - `by_id(discovery_id: int, team: Team) -> SearchResult[Piece]`: Find team owner by its id on the given `team`.
    
    - `by_name(name: str, team: Team) -> SearchResult[Piece]`: Find team owner by its name on the given `team`.
    
    - `by_roster_number(roster_number: int, team: Team) -> SearchResult[Piece]`: Find team owner by its roster number
      on the given team. Roster numbers are unique within team team. Not unique across teams.
      
    - `hostage_by_idy(discovery_id: int, team: Team) -> SearchResult[CombatantPiece]`:
      
    - `by_rank(rank: Rank, team: Team) -> SearchResult[list[Piece]]`: A list of all members with `rank` on 
      given team. of team specific rank within team team.

  Note:
    DO NOT USE ANY OTHER METHODS TO SEARCH A TEAM. USE ONLY THE METHODS IN THIS CLASS.

  See Also:
    `Team`: The team being searched
    `Piece`: The owner being searched for
    `SearchResult`: The return type for all old_search operations
  """

  @classmethod
  def search(cls, team: Team, data_source: PieceCollection, search_context: SearchContext) -> SearchResult[List[Piece]]:
    """
    Action:
    Parameters:
        * `param` (`DataType`):
    Returns:
        `DataType` or `Void`
    Raises:
    MethodNameException wraps
        *
    """
    method = "ClassName.method_name"

    validation = TeamValidator.validate(team)
    if not validation.is_success():
      return SearchResult(exception=validation.exception)

    if data_source == PieceCollection.ROSTER:
      return TeamRosterSearch.search(team=team, search_context=search_context)
    else:
      return TeamHostageSearch.search(team=team, search_context=search_context)
