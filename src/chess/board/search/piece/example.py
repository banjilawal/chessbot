# src/chess/board_validator/board_validator.py
"""
Module: chess.board_validator.board_validator
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation 1***: No coord_stack_validator, error checking is performed in `Board` class. Using the class directly instead of
  its CRUD interfaces goes against recommended usage.

***Limitation 2***: There is no guarantee properly created `Board` objects released by the module will satisfy client
    requirements. Clients are responsible for ensuring a `BoardBuilder` product will not fail when used. Products
    from `BoardBuilder` --should-- satisfy `BoardValidator` requirements.

**Related Features**:
    Authenticating existing boards -> See BoardValidator, module[chess.board_validator.coord_stack_validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data Holding, Coordination, Performance

**Design Concepts**:
    Separating object creation from object usage.
    Keeping constructors lightweight

# PURPOSE:
---------
1. Putting all the steps and logging into one place makes modules using `Board` objects cleaner and easier to follow.

***Satisfies***: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
    `BuildResult`, `Builder`, `LoggingLevelRouter`, `ChessException`, `NullException`, `BuildFailedException`
    `IdValidator`, `NameValidator`

From `chess.board_validator`:
    `Board`, `NullBoard`, `BoardBuildFailedException`, `BoardSchema`

From `chess.player_agent`:
  `PlayerAgent`, `PlayerAgentValidator`,

From `chess.owner`:
  `Piece`

# CONTAINS:
----------
 * `Board`
"""