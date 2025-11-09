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

from chess.piece import Piece
from chess.team import Team, TeamSearchContext, TeamValidator
from chess.system import Search, SearchResult
from chess.team.search import PieceSearchContextValidator


class TeamHostageSearch(Search):
  """
  # ROLE: Builder implementation

  # RESPONSIBILITIES:
  1. Process and validate parameters for creating `Team` instances.
  2. Create new `Team` objects if parameters meet specifications.
  2. Report errors and return `BuildResult` with error details.

  # PROVIDES:
  `BuildResult`: Return type containing the built `Team` or error information.

  # ATTRIBUTES:
  None
  """
  @classmethod
  def search(cls, team: Team, search_context: TeamSearchContext) -> SearchResult[List[Piece]]:
      method = "DiscoverySearch.old_search"

      team_validation = TeamValidator.validate(team)
      if not team_validation.is_success():
        return SearchResult(exception=team_validation.exception)

      search_context_validation = PieceSearchContextValidator.validate(search_context)
      if not search_context_validation.is_success():
        return SearchResult(exception=search_context_validation.exception)


      if search_context.name is not None:
        return TeamHostageSearch._name_search(team=team, name=search_context.name)

      if search_context.rank is not None:
        return TeamHostageSearch._rank_filter(team=team, rank=search_context.rank)

      if search_context.ransom is not None:
        return TeamHostageSearch._ransom_filter(team=team, ransom=search_context.ransom)

      if search_context.piece_id is not None:
        return TeamHostageSearch._id_search(team=team, piece_id=search_context.piece_id)

      if search_context.roster_number is not None:
        return TeamHostageSearch. _roster_number_search(team=team, roster_number=search_context.roster_number)

  @classmethod
  def _name_search(cls, team: Team, name: str) -> SearchResult[List[Piece]]:
      """
      Does not guarantee uniqueness returns the first item which duplicates the given name.
      """
      method = "DiscoverySearch._name_search"

      prisoner = next((hostage for hostage in team.hostages if hostage.name.upper() == name.upper()), None)
      if prisoner is not None:
          return SearchResult(payload=List[prisoner])

      # returns empty old_search notification if no consistency ws found
      return SearchResult()

  @classmethod
  def _rank_filter(cls, team: Team, rank: Rank) -> SearchResult[List[Piece]]:
      matches = [hostage for hostage in team.hostages if hostage.rank == rank]
      return SearchResult(payload=matches)

  @classmethod
  def _ransom_filter(cls, team: Team, ransom: int) -> SearchResult[List[Piece]]:
      matches = [hostage for hostage in team.hostages if hostage.rank.ransom == ransom]
      return SearchResult(payload=matches)

  @classmethod
  def _id_search(cls, team: Team, piece_id: int) -> SearchResult[List[Piece]]:
      """
      IDs should be unique. Faster old_search would return the first consistency. An easy
      integrity check finds all the items with the same id. If there is more than
      one raise team `DuplicateUniqueIdException`.

      Performance Impact:
      The set of hostages will never exceed 15 so this is not going to be team really
      burdensome old_search.
      """
      method = "DiscoverySearch._id_search"

      prisoner = next((hostage for hostage in team.hostages if hostage.id == piece_id), None)
      if prisoner is not None:
          return SearchResult(payload=List[prisoner])

      # returns empty old_search notification if no consistency ws found
      return SearchResult()

  @classmethod
  def _roster_number_search(cls, team: Team, roster_number: int) -> SearchResult[List[Piece]]:
      """
      Does not guarantee uniqueness returns the first item which duplicates the given id.
      """
      method = "DiscoverySearch._roster_number_search"

      prisoner = next((hostage for hostage in team.hostages if hostage.roster_number == roster_number), None)
      if prisoner is not None:
          return SearchResult(payload=List[prisoner])

      # returns empty old_search notification if no consistency ws found
      return SearchResult()