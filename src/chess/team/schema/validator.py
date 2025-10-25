# src/chess/teamSchema/schema/old_occupation_validator.py

"""
Module: chess.teamSchema.validator
Author: Banji Lawal
Created: 2025-10-08

# SCOPE:
-------
***Limitation 1***: This module cannot prevent classes, processes or modules using `TeamSchema`
    instances that pass sanity checks will not fail when using the validated `TeamSchema`.
    Once client's processes might fail, experience data inconsistency or have other
    faults.

***Limitation 2***: Objects authenticated by `TeamSchemaValidator` might fail additional requirements
    a client has for a `TeamSchema`. It is the client's responsibility to ensure the validated
    `TeamSchema` passes and additional checks before deployment.

***Related Features***:
    Building teamSchemas -> See TeamSchemaBuilder, module[chess.teamSchema.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data assurance, error detection, error prevention

# PURPOSE:
---------
1. Central, single source of truth for correctness of existing `TeamSchema` objects.
2. Putting all the steps and logging into one place makes modules using `TeamSchema` objects
    cleaner and easier to follow.

***Satisfies***: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
  * `ValidationResult`, `Validator`, `LoggingLevelRouter`

From `chess.teamSchema`:
    `TeamSchema`, `NullTeamSchemaException`, `InvalidTeamSchemaException`, `NullXComponentException`,
    `NullYComponentException`, `TeamSchemaBelowBoundsException`, `TeamSchemaAboveBoundsException`

# CONTAINS:
----------
 * `TeamSchemaValidator`
"""

from typing import cast

from chess.system import ValidationResult, Validator, LoggingLevelRouter
from chess.team import TeamSchema, NullTeamSchemaException, InvalidTeamSchemaException


class TeamSchemaValidator(Validator[TeamSchema]):
  """
  # ROLE: Validation

  # RESPONSIBILITIES:
  1. Prevents using an existing TeamSchema` that will cause failures or introduce bugs if deployed.
  2. Ensures clients receive only valid TeamSchemas for further processing.
  3. Sending granular error report via `ValidationResult`.

  # PROVIDES:
    `ValidationResult`: Return type containing the built `TeamSchema` or error information.

  # ATTRIBUTES:
  None
  """

  @classmethod
  @LoggingLevelRouter.monitor()
  def validate(cls, candidate: TeamSchema) -> ValidationResult[TeamSchema]:
    """
    ACTION:
      Ensure an existing `TeamSchema` object will not introduce bugs or failures.

    PARAMETERS:
        * `candidate` (`TeamSchema`): The validator candidate.

    RETURNS:
    `ValidationResult[TeamSchema]`: A `ValidationResult` containing either:
        `'payload'` - A `TeamSchema` instance that satisfies the specification.
        `rollback_exception` - Details about which specification violation occurred.

    RAISES:
    `InvalidTeamSchemaException`: Wraps any specification violations including:
      `TypeError`: if `candidate` is not a `TeamSchema` object
      `NullTeamSchemaException`: if `candidate` is null
    """
    method = "TeamSchemaValidator.validate"

    try:
      if candidate is None:
        return ValidationResult(exception=
            NullTeamSchemaException(f"{method} {NullTeamSchemaException.DEFAULT_MESSAGE}"
        ))

      if not isinstance(candidate, TeamSchema):
        return ValidationResult(exception=TypeError(
          f"{method} Expected teamSchema TeamSchema, got {type(candidate).__name__}"
        ))

      team_schema = cast(TeamSchema, candidate)
      return ValidationResult(payload=team_schema)

    except Exception as e:
      return ValidationResult(exception=InvalidTeamSchemaException(f"{method}: {e}"))