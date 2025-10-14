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

from typing import Sequence

from chess.piece import Piece
from chess.system import AutoId
from chess.commander import Commander
from chess.team import TeamSchema


@AutoId()
class Team:
  """
  # ROLE: Service, Coordination

  # RESPONSIBILITIES:
  # PROVIDES:

  ATTRIBUTES:
    * `_commander` (`Commander`): Player who controls `Team`
    * `_schema` (`TeamSchema`): Specs about `Team` eg color, starting squares, name.
    * `_roster` (`List[Piece]`): List of chess pieces on the team.
    * `_hostages` (`List[Piece]`): List of captured enemy pieces.
  """

  id: int
  _commander: Commander
  _schema: TeamSchema
  _roster: list['Piece']
  _hostages: list['Piece']

  def __init__(self, commander: Commander, schema: TeamSchema):
    method = "Team.__init__"
    self._commander = commander
    self._schema = schema
    self._roster = []


  @property
  def commander(self) -> 'Commander':
    return self._commander


  @property
  def schema(self) -> TeamSchema:
    return self._schema


  @property
  def roster(self) -> Sequence['Piece']:
    """
    Returns team read-only view of the team's roster. The returned sequence is safe to
    iterate and index, but mutating it will not affect the original roster.
    """
    return self._roster.copy()


  @property
  def hostages(self) -> Sequence['Piece']:
    """
    Returns team read-only view of the team's rostages. The returned sequence is safe to
    iterate and index, but mutating it will not affect the original hostage list.
    """
    return self._hostages.copy()


  def add_to_roster(self, piece: Piece):
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
    method = "Team.add_to_roster"
    self._roster.append(piece)


  def remove_from_roster(self, piece):
    if piece in self._roster:
      self._roster.remove(piece)


  def add_hostage(self, enemy: Piece):
    if enemy not in self._hostages:
      self._hostages.append(enemy)


  def remove_hostage(self, enemy: Piece):
    if enemy in self._hostages:
      self._hostages.remove(enemy)


  def __eq__(self, other):
    if other is self:
      return True
    if other is None:
      return False
    if not isinstance(other, 'Team'):
      return False
    return self.id == other.id


  def __hash__(self):
    return hash(self.id)


  def __str__(self):
    return f"Team[id:{self.id} commander:{self._commander.name} {self._schema}"