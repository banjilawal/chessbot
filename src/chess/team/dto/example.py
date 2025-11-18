src / chess / team / old_occupation_validator.py

"""
Module: chess.team_name.validator
Author: Banji Lawal
Created: 2025-09-04
Updated: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation***: There is no guarantee properly created `Team` objects released by the module will satisfy
    client requirements. Clients are responsible for ensuring a `TeamBuilder` product will not fail when used.

**Related Features**:
    Authenticating existing teams -> See TeamValidator, module[chess.team_name.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data assurance, error prevention

**Design Concepts**:
    Separating object creation from object usage.
    Keeping constructors lightweight

# PURPOSE:
---------
1. Central, single producer of authenticated `Team` objects.
2. Putting all the steps and logging into one place makes modules using `Team` objects cleaner and easier to follow.

**Satisfies**: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
    `BuildResult`, `Builder`, `LoggingLevelRouter`, `ChessException`, `NullException`, `BuildFailedException`
    `IdValidator`, `NameValidator`

From `chess.team_name`:
    `Team`, `NullTeam`, `TeamBuildFailedException`, `TeamSchema`

From `chess.agent`:
  `Agent`, `PlayerAgentValidator`,

# CONTAINS:
----------
 * `TeamBuilder`
"""
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
"""
ACTION:
Create a `Team` object if the parameters have correctness.

PARAMETERS:
    * `agent` (`Agent`): owner of `Team` object.
    * `schema` (`iTeamSchema`): Spec about the team_name's color, starting squares etc.

RETURNS:
`BuildResult[Team]`: A `BuildResult` containing either:
    `'payload'` - A valid `Team` instance in the payload
    `rollback_exception` - Error information and error details

RAISES:
`TeamBuildFailedException`: Wraps any specification violations including:
    * `NullXComponentException`: if `x` is None
    * `NullYComponentException`: if `y` is None
    * `TeamBelowBoundsException`: if `x` or `y` < -LONGEST_KNIGHT_LEG_SIZE
    * `TeamAboveBoundsException`: if `x` or `y` > LONGEST_KNIGHT_LEG_SIZE
"""