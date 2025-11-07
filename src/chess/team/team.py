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

from typing import List, Optional, Sequence, cast

from chess.piece import KingPiece, Piece
from chess.system import AutoId
from chess.commander import Commander
from chess.team import Team, TeamSchema


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
    MAX_ROSTER_SIZE = 16
    
    _id: int
    _commander: Commander
    _schema: TeamSchema
    _roster: list['Piece']
    _hostages: list['Piece']
    _enemy_king: KingPiece
    
    def __init__(self, id: int, commander: Commander, schema: TeamSchema):
        """"""
        method = "Team.__init__"
        self._id = id
        self._commander = commander
        self._schema = schema
        self._roster = []
        self._hostages = []
        self._hostages = None
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def commander(self) -> 'Commander':
        return self._commander
    
    @property
    def schema(self) -> TeamSchema:
        return self._schema
    
    @property
    def roster(self) -> List[Piece]:
        return self._roster
    
    @property
    def hostages(self) -> List[Piece]:
        return self._hostages
    
    @property
    def enemy_king(self) -> Optional[KingPiece]:
        return self._enemy_king
    
    @enemy_king.setter
    def enemy_king(self, enemy_king: KingPiece):
        self._enemy_king = enemy_king
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Team):
            team = cast(Team, other)
            return self._id == team._id
        
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"Team{id:{self._id} commander:{self._commander.name} {self._schema}}"
