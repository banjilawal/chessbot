# src/chess/piece/event/transaction
"""
Module: chess.piece.event.transaction
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
* The limits of the module, defined by what it does not do.
* Where to look for related features this models does not provide because of its limitations.

# THEME:
* Highlight the core feature (thread-safety)
* Explain the how-and-why of implementation choices.

# PURPOSE:
* Function and role in the system.
* Why the module exists in the application architecture
* What problem it fundamentally solves

# DEPENDENCIES:

# CONTAINS:
 * `OccupationTransaction`
"""

from enum import auto, Enum
from re import search
from typing import List

from chess.team import Team, TeamValidator
from chess.piece.piece import Piece
from chess.search import SearchResult
from chess.rank import Rank, RankValidator
from chess.system import IdValidator, NameValidator, Search, SearchContext
from chess.team.search import TeamHostageSearch, TeamRosterSearch, Datasource


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
  Static methods for entities and operations that need to search team Team for pieces and ranks. Provides consistent
  search interface and return types across all search operations. Validates input parameters before searching to
  ensure safe operations. Returns SearchResult objects encapsulating either the found entity or error information.

  Usage:
  ```python
    from chess.team import Team, TeamSearch
    from chess.piece import Piece
   ```
   
  Methods:
    - `by_id(discovery_id: int, team: Team) -> SearchResult[Piece]`: Find team piece by its id on the given `team`.
    
    - `by_name(name: str, team: Team) -> SearchResult[Piece]`: Find team piece by its name on the given `team`.
    
    - `by_roster_number(roster_number: int, team: Team) -> SearchResult[Piece]`: Find team piece by its roster number
      on the given team. Roster numbers are unique within team team. Not unique across teams.
      
    - `hostage_by_idy(discovery_id: int, team: Team) -> SearchResult[CombatantPiece]`:
      
    - `by_rank(rank: Rank, team: Team) -> SearchResult[list[Piece]]`: A list of all members with `rank` on 
      given team. of team specific rank within team team.

  Note:
    DO NOT USE ANY OTHER METHODS TO SEARCH A TEAM. USE ONLY THE METHODS IN THIS CLASS.

  See Also:
    `Team`: The team being searched
    `Piece`: The piece being searched for
    `SearchResult`: The return type for all search operations
  """

  @classmethod
  def search(cls, team: Team, data_source: Datasource, search_context: SearchContext) -> SearchResult[List[Piece]]:
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

    if data_source == Datasource.ROSTER:
      return TeamRosterSearch.search(team=team, search_context=search_context)
    else:
      return TeamHostageSearch.search(team=team, search_context=search_context)
