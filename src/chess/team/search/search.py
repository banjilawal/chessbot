# src/chess/team_name/team_name.py
"""
Module: chess.team_name.team_name
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation 1***: No coord_stack_validator, error checking is performed in `Team` class. Using the class directly instead of
  its CRUD interfaces goes against recommended usage.

***Limitation 2***: There is no guarantee properly created `Team` objects released by the module will satisfy client
    requirements. Clients are responsible for ensuring a `TeamBuilder` product will not fail when used. Products
    from `TeamBuilder` --should-- satisfy `TeamValidator` requirements.

**Related Features**:
    Authenticating existing teams -> See TeamValidator, module[chess.team_name.coord_stack_validator],
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

From `chess.team_name`:
    `Team`, `NullTeam`, `TeamBuildFailedException`, `TeamSchema`

From `chess.agent`:
  `Agent`, `PlayerAgentValidator`,

From `chess.owner`:
  `Piece`

# CONTAINS:
----------
 * `Team`
"""

from typing import List

from chess.team import Team, TeamSearchContext, TeamValidator
from chess.piece.piece import Piece
from chess.agent.search import SearchResult
from chess.system import SearchContext
from chess.team.search import TeamHostageSearch, TeamRosterSearch, PieceCollectionCategory


class TeamSearch(Piece):
  """
  # ROLE: Search

  # RESPONSIBILITIES:
  Find Team instances that match target attributes set in TeamContext

  # PROVIDES:
  SearchResult[List[Team]' containing either:
      - On success: List[Team] in the payload.
      - On failure: Exception.

  # ATTRIBUTES:
  No attributes

  # CONSTRUCTOR:
  Default Constructor

  # CLASS METHODS:
      ## search signature:
              def search(
                      cls,
                      data_set: List[Team],
                      search_context: TeamSearchContext
              ) -> SearchResult[List[Piece]]:
              
  # INSTANCE METHODS:
  None
  """

  @classmethod
  def search(
          cls,
          data_set: List[Team],
          search_context: TeamSearchContext
  ) -> SearchResult[List[Piece]]:
    """"""
    method = "TeamSearch.search"

    validation = TeamValidator.validate(team)
    if not validation.is_success():
      return SearchResult(exception=validation.exception)

    if data_source == PieceCollectionCategory.ROSTER:
      return TeamRosterSearch.search(team=team, search_context=search_context)
    else:
      return TeamHostageSearch.search(team=team, search_context=search_context)
