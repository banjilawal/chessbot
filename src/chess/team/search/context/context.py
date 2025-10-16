# src/chess/team/team.py
"""
Module: chess.team.team
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation 1***: No validation, error checking is performed in `Team` class. Using the class directly instead of
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

From `chess.piece`:
  `Piece`

# CONTAINS:
----------
 * `Team`
"""

from typing import Optional

from chess.rank import Rank
from chess.system import SearchContext

class TeamSearchContext(SearchContext):
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
  _name: Optional[str] = None
  _rank: Optional[Rank] = None
  _ransom: Optional[int] = None,
  _piece_id: Optional[int] = None
  _roster_number: Optional[int] = None

  def __init__(
      self,
      name: Optional[str] = None,
      rank: Optional[Rank] = None,
      ransom: Optional[int] = None,
      piece_id: Optional[int]=None,
      roster_number: Optional[int]=None
  ):
    self._name = name
    self._rank = rank
    self._ransom = ransom
    self._piece_id = piece_id
    self._roster_number = roster_number

@property
def name(self) -> Optional[str]:
  return self._name

@property
def rank(self) -> Optional[Rank]:
  return self._rank

@property
def ransom(self) -> Optional[int]:
  return self._ransom

@property
def piece_id(self) -> Optional[int]:
  return self._piece_id

@property
def roster_number(self) -> Optional[int]:
  return self._roster_number



def to_dict(self) -> dict:
  return {
    "name": self._name,
    "rank": self._rank,
    "ransom": self._ransom,
    "id": self._piece_id,
    "roster_number": self._roster_number,
  }