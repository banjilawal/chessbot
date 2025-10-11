# src/chess/team/validation.py

"""
Module: chess.team.validator
Author: Banji Lawal
Created: 2025-09-11
Updated: 2025-10-08

# SCOPE:
-------
**Limitation**: This module cannot prevent classes, processes or modules using `Team`
    instances that pass sanity checks will not fail when using the validated `Team`.
    Once client's processes might fail, experience data inconsistency or have other
    faults.
**Limitation**: Objects authenticated by `TeamValidator` might fail additional requirements
    a client has for a `Team`. It is the client's responsibility to ensure the validated
    `Team` passes and additional checks before deployment.

**Related Features**:
    Building teams -> See TeamBuilder, module[chess.team.builder],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data assurance, error detection, error prevention

# PURPOSE:
---------
1. Central, single source of truth for correctness of existing `Team` objects.
2. Putting all the steps and logging into one place makes modules using `Team` objects
    cleaner and easier to follow.

**Satisfies**: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
  * `ValidationResult`, `Validator`, `LoggingLevelRouter`

From `chess.team`:
    `Team`, `NullTeamException`, `InvalidTeamException`, `NullXComponentException`,
    `NullYComponentException`, `TeamBelowBoundsException`, `TeamAboveBoundsException`

# CONTAINS:
----------
 * `TeamValidator`
"""
from typing import cast
from chess.commander import Commander, CommanderValidator, InvalidCommanderAssignmentException
from chess.team import Team, InvalidTeamException, NullTeamException, NullTeamSchemaException, TeamSchemaValidator
from chess.system import ValidationResult, Validator, LoggingLevelRouter, IdValidator, InconsistentCollectionException


class TeamValidator(Validator[Team]):
  """
  # ROLE: Validation

  # RESPONSIBILITIES:
  1. Prevents using an existing Team` that will cause failures or introduce bugs if deployed.
  2. Ensures clients receive only valid Teams for further processing.
  3. Sending granular error report via `ValidationResult`.

  # PROVIDES:
    `ValidationResult`: Return type containing the built `Team` or error information.

  # ATTRIBUTES:
  None
  """

  @classmethod
  @LoggingLevelRouter.monitor()
  def validate(cls, candidate: Team) -> ValidationResult[Team]:
    """
    ACTION:
      Ensure an existing `Team` object will not introduce bugs or failures.

    PARAMETERS:
        * `candidate` (`Team`): The validation candidate.

    RETURNS:
    `ValidationResult[Team]`: A `ValidationResult` containing either:
        `'payload'` - A `Team` instance that satisfies the specification.
        `exception` - Details about which specification violation occurred.

    RAISES:
    `InvalidTeamException`: Wraps any specification violations including:
      `TypeError`: if `candidate` is not team Team` object
      `NullTeamException`: if `candidate` is null
      `InvalidIdException`: if `id` fails validate checks
      `InvalidCommanderException`: if `commander` fails validate checks
      `NullTeamProfileException`: if `schema` is null
      `InvalidCommanderAssignmentException`: if the assigned commander does not match the validated commander
      `RelationshipException`: if the bidirectional relationship between Team and Commander is broken
    """
    method = "TeamValidator.validate"

    try:
      if candidate is None:
        return ValidationResult(exception=
            NullTeamException(f"{method} {NullTeamException.DEFAULT_MESSAGE}"
        ))

      from chess.team import Team
      if not isinstance(candidate, Team):
        return ValidationResult(exception=TypeError(
          f"{method} Expected team Team, got {type(candidate).__name__}"
        ))

      team = cast(Team, candidate)

      schema_validation = TeamSchemaValidator.validate(team.schema)
      if not schema_validation.is_success():
        return ValidationResult(exception=schema_validation.exception)

      id_validation = IdValidator.validate(team.id)
      if not id_validation.is_success():
        return ValidationResult(exception=id_validation.exception)

      commander_validation = CommanderValidator.validate(team.commander)
      if not commander_validation.is_success():
        return ValidationResult(exception=commander_validation.exception)

      commander = cast(Commander, commander_validation.payload)
      if team.commander != commander:
        return ValidationResult(exception=InvalidCommanderAssignmentException(
          f"{method}: {InvalidCommanderAssignmentException.DEFAULT_MESSAGE}"
        ))

      if team not in commander.teams.items:
        return ValidationResult(exception=InconsistentCollectionException(
          f"{method}: [Team-Not-In-Commander-History] {InconsistentCollectionException.DEFAULT_MESSAGE}"
        ))

      return ValidationResult(payload=team)

    except Exception as e:
      return ValidationResult(exception=InvalidTeamException(f"{method}: {e}"))