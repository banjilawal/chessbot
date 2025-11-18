# src/chess/team_name/schema/schema.py
"""
Module: chess.team_name.schema.schema
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
    Authenticating existing teams -> See TeamValidator, module[chess.team_name.validator],
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

from enum import Enum
from chess.scalar import Scalar
from chess.geometry import Quadrant
from chess.system import GameColor, ROW_SIZE


class TeamSchema(Enum):
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

  def __new__(
    cls,
    game_color: GameColor,
    rank_row: int,
    advancing_step: Scalar,
    home_quadrant: Quadrant
  ):
    obj = object.__new__(cls)
    obj._game_color = game_color
    obj._rank_row = rank_row
    obj._advancing_step = advancing_step
    obj._home_quadrant = home_quadrant

    return obj

  WHITE = (GameColor.WHITE, 0, Scalar(1), Quadrant.N)
  BLACK = (GameColor.BLACK, (ROW_SIZE - 1), Scalar(-1), Quadrant.S)


  @property
  def letter(cls) -> str:
    return cls.name[0]


  @property
  def color(self) -> GameColor:
    return self._game_color


  @property
  def advancing_step(self) -> Scalar:
    return self._advancing_step

  @property
  def home_quadrant(self) -> Quadrant:
    return self.home_quadrant


  @property
  def rank_row(self) -> int:
    return self._rank_row


  @property
  def pawn_row(self) -> int:
    return self._rank_row + self._advancing_step.value


  @property
  def enemy_schema(self) -> 'TeamSchema':
    return TeamSchema.BLACK if self == TeamSchema.WHITE else TeamSchema.WHITE
  
  
  def schema_from_color(self, color: GameColor) -> 'TeamSchema':
    if color == TeamSchema.WHITE:
      return TeamSchema.WHITE
    return TeamSchema.BLACK


  def __str__(self) -> str:
    return (
      f"color:{self._game_color.name}, "
      f"advancing_step:{self._advancing_step} "
      f"rank_row:{self.rank_row} "
      f"pawn_row:{self.pawn_row}]"
    )


# def main():
#
#   for schema in TeamProfile:
#     print(schema)
#
#
# if __name__ == "__main__":
#   main()