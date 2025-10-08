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

from typing import cast, Generic, TYPE_CHECKING, TypeVar

from chess.system import Result, Validator, IdValidator, InvalidIdException
from chess.exception import RelationshipException
from chess.team import Team, NullTeamException, NullTeamSchemaException, InvalidTeamException
from chess.commander import Commander, CommanderValidator, InvalidCommanderException, \
  InvalidCommanderAssignmentException

T = TypeVar('T')

class TeamValidator(Validator):
  """
  ROLE:
  ----
  RESPONSIBILITIES:
  ----------------
  PROVIDES:
  --------
  ATTRIBUTES:
  ----------
  [
    <No attributes. Implementors declare their own.>
  OR
    * `_attribute` (`data_type`): <sentence_if_necessary>
  ]
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
  def validate(candidate: Team) -> Result['Team']:
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
      `InvalidIdException`: if `id` fails validate checks
      `InvalidCommanderException`: if `commander` fails validate checks
      `NullTeamProfileException`: if `profile` is null
      `InvalidCommanderAssignmentException`: if the assigned commander does not match the validated commander
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

      if team.scheme is None:
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
        raise RelationshipException(f"{method}: {RelationshipException.DEFAULT_MESSAGE}")

      return Result(payload=team)

    except (
        TypeError,
        NullTeamException,
        InvalidIdException,
        NullTeamSchemaException,
        InvalidCommanderException,
        InvalidCommanderAssignmentException,
        RelationshipException
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
#   team = Team(team_id=1, controller=person, profile=TeamProfile.BLACK)
#
#
# if __name__ == "__main__":
#   main()