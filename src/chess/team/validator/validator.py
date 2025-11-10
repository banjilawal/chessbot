# src/chess/team_name/validator/validator.py

"""
Module: chess.team_name.validator.validator
Author: Banji Lawal
Created: 2025-09-11
Updated: 2025-10-08

# SCOPE:
-------
**Limitation**: This module cannot prevent classes, processes or modules using `Team`
    instances that pass sanity checks will not fail when using the validated `Team`.
    Once client's processes might fail, experience service inconsistency or have other
    faults.
**Limitation**: Objects authenticated by `TeamValidator` might fail additional requirements
    a client has for a `Team`. It is the client's responsibility to ensure the validated
    `Team` passes and additional checks before deployment.

**Related Features**:
    Building teams -> See TeamBuilder, module[chess.team_name.validator],
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

From `chess.team_name`:
    `Team`, `NullTeamException`, `InvalidTeamException`, `NullXComponentException`,
    `NullYComponentException`, `TeamBelowBoundsException`, `TeamAboveBoundsException`

# CONTAINS:
----------
 * `TeamValidator`
"""

from typing import cast, Any


from chess.system import ValidationResult, Validator, LoggingLevelRouter, IdValidator
from chess.commander import Commander, CommanderValidator, InvalidCommanderAssignmentException
from chess.team import Team, NullTeamException, TeamFieldConsistencyCheck, TeamCommanderInconsistencyException


class TeamValidator(Validator[Team]):
  """
  # ROLE: Validation

  # RESPONSIBILITIES:
  1. Ensures clients receive only valid Teams for further processing.
  2 Sending granular error report via `ValidationResult`.

  # PROVIDES:
    `ValidationResult[Team]`: Contains either a verified `Team` or an `Exception`.

  # ATTRIBUTES:
  None
  """

  @classmethod
  @LoggingLevelRouter.monitor()
  def validate(cls, candidate: Any) -> ValidationResult[Team]:
    """
    ACTION:
      Ensure an existing `Team` object will not introduce bugs or failures.

    PARAMETERS:
        * `candidate` (`Any`): The validator candidate.

    RETURNS:
    `ValidationResult[Team]`: A `ValidationResult` containing either:
        `'payload'` - A `Team` instance that satisfies the specification.
        `rollback_exception` - Details about which specification violation occurred.

    RAISES:
    `InvalidTeamException`: Wraps any specification violations including:
      `TypeError`: if `candidate` is not team_name Team` object
      `NullTeamException`: if `candidate` is null
      `InvalidIdException`: if `visitor_id` fails validate checks
      `InvalidCommanderException`: if `commander` fails validate checks
      `NullTeamProfileException`: if `schema` is null
      `InvalidCommanderAssignmentException`: if the assigned commander does not consistency the validated commander
      `RelationshipException`: if the bidirectional relationship between Team and Commander is broken
    """
    method = "TeamValidator.validate"

    try:
      if candidate is None:
        return ValidationResult.failure(NullTeamException(f"{method} {NullTeamException.DEFAULT_MESSAGE}")
        )

      if not isinstance(candidate, Team):
        return ValidationResult.failure(
          TypeError(f"{method} Expected team_name Team, got {type(candidate).__name__}")
        )

      team = cast(Team, candidate)
      
      id_validation = IdValidator.validate(team.id)
      if not id_validation.is_success():
        return ValidationResult.failure(id_validation.exception)
      
      name_consistency = TeamFieldConsistencyCheck.team_name_consistency((team, team.schema.name))
      if name_consistency.failure():
        return ValidationResult.failure(name_consistency.exception)
      
      letter_consistency = TeamFieldConsistencyCheck.team_letter_consistency((team, team.schema.letter))
      if letter_consistency.failure():
        return ValidationResult.failure(letter_consistency.exception)
      
      rank_row_consistency = TeamFieldConsistencyCheck.team_rank_row_consistency((team, team.schema.rank_row))
      if rank_row_consistency.failure():
        return ValidationResult.failure(rank_row_consistency.exception)
      
      pawn_row_consistency = TeamFieldConsistencyCheck.team_pawn_row_consistency((team, team.schema.rank_row))
      if pawn_row_consistency.failure():
        return ValidationResult.failure(pawn_row_consistency.exception)
      
      color_consistency = TeamFieldConsistencyCheck.team_color_consistency((team, team.schema.color))
      if color_consistency.failure():
        return ValidationResult.failure(color_consistency.exception)

      commander_validation = CommanderValidator.validate(team.commander)
      if not commander_validation.is_success():
        return ValidationResult.failure(commander_validation.exception)

      commander = cast(Commander, commander_validation.payload)
      if team.commander != commander:
        return ValidationResult.failure(
          InvalidCommanderAssignmentException(f"{method}: {InvalidCommanderAssignmentException.DEFAULT_MESSAGE}")
        )

      if team not in commander.teams.items:
        return ValidationResult.failure(
            TeamCommanderInconsistencyException(f"{method}:  {TeamCommanderInconsistencyException.DEFAULT_MESSAGE}")
        )

      return ValidationResult.success(team)

    except Exception as e:
      return ValidationResult.failure(e)