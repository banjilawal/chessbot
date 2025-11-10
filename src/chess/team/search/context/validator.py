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

from typing import cast, Generic, TYPE_CHECKING, TypeVar

from chess.system import Result, Validator, IdValidator, InvalidIdException, InconsistentCollectionException
from chess.team import Team, NullTeamException, NullTeamSchemaException, InvalidTeamException
from chess.commander import Commander, CommanderValidator, InvalidCommanderException, \
  InvalidCommanderAssignmentException
from chess.team.search import TeamSearchContext

T = TypeVar('T')

class PieceSearchContextValidator(Validator):
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
  Validates existing `Team` instances that are passed around the system.

  While `TeamBuilder` ensures valid Teams are created, `TeamValidator`
  checks `Team` instances that already exist - whether they came from
  deserialization, external sources, or need re-validate after modifications.
  
  Usage:
    ```python
    # Validate an existing team
    team_validation = TeamValidator.validate(candidate)  
    if not team_validation.is_success():
      raise team_validation.err
    team = cast(Team, team_validation.payload)
    ```

  Use `TeamBuilder` for construction, `TeamValidator` for verification.
  """

  @staticmethod
  def validate(candidate: TeamSearchContext) -> Result[TeamSearchContext]:
    """
    Validates that an existing `Team` instance meets all specifications.

    Performs comprehensive validate on team `Team` instance that already exists,
    checking type safety, null values, and component bounds. Unlike `TeamBuilder`
    which creates new valid Teams, this validator verifies existing `Team`
    instances from external sources, deserialization, or after modifications.

    Args
      `candidate` (`Team`): `Team` instance to validate

     Returns:
      `Result`[`Team`]: A `Resul`candidate object containing the validated payload if the specification is satisfied,
      `InvalidTeamException` otherwise.

    Raises:
      `TypeError`: if `candidate` is not team Team` object
      `NullTeamException`: if `candidate` is null
      `InvalidIdException`: if `visitor_id` fails validate checks
      `InvalidCommanderException`: if `commander` fails validate checks
      `NullTeamProfileException`: if `schema` is null
      `InvalidCommanderAssignmentException`: if the assigned commander does not consistency the validated commander
      `RelationshipException`: if the bidirectional relationship between Team and Commander is broken
      `InvalidTeamException`: Wraps any preceding exceptions
    """
    method = "TeamValidator.validate"

    try:
      if candidate is None:
        raise NullTeamException(f"{method} {NullTeamException.DEFAULT_MESSAGE}")

      from chess.team import Team
      if not isinstance(candidate, Team):
        raise TypeError(f"{method} Expected team Team, got {type(candidate).__name__}")

      team = cast(Team, candidate)

      if team.schema is None:
        raise NullTeamSchemaException(f"{method}: {NullTeamSchemaException.DEFAULT_MESSAGE}")

      id_validation = IdValidator.validate(team.id)
      if not id_validation.is_success():
        raise InvalidIdException(f"{method}: {InvalidIdException.DEFAULT_MESSAGE}")

      commander_validation = CommanderValidator.validate(team.commander)
      if not commander_validation.is_success():
        raise InvalidCommanderException(f"{method}: {InvalidCommanderException.DEFAULT_MESSAGE}")

      commander = cast(Commander, commander_validation.payload)
      if team.commander != commander:
        raise InvalidCommanderAssignmentException(
          f"{method}: {InvalidCommanderAssignmentException.DEFAULT_MESSAGE}"
        )

      if team not in commander.teams.items:
        raise InconsistentCollectionException(
          f"{method}: [Team-Not-In-Commander-History] {RelationshipException.DEFAULT_MESSAGE}"
        )

      return Result(payload=team)

    except (
        TypeError,
        NullTeamException,
        InvalidIdException,
        NullTeamSchemaException,
        InvalidCommanderException,
        InconsistentCollectionException,
        InvalidCommanderAssignmentException,
    ) as e:
      raise InvalidTeamException(f"{method}: {InvalidTeamException.DEFAULT_MESSAGE}") from e

    # This block catches any unexpected exceptions
    # You might want to log the error here before re-raising
    except Exception as e:
      raise InvalidTeamException(f"An unexpected error occurred during validate: {e}") from e

#
# def main():
#
#   from chess.commander.commander import Human
#   person = Human(1, "person")
#
#   from chess.team import Team
#   team = Team(visitor_team_id=1, controller=person, schema=TeamProfile.BLACK)
#
#
# if __name__ == "__main__":
#   main()