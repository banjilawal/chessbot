# src/model/binder/validation/validation.py

"""
Module: model.binder.validation.validation
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Any, cast

from model.catalog import SchemaService
from system import LoggingLevelRouter, Validator
from result.result.result import ValidationResult
from model.team import (
    BlackTeamHasWrongSchemaException, TeamBinder, TeamBinderNullException, TeamBinderValidationException,
    TeamValidator, WhiteTeamHasWrongSchemaException
)


class TeamBinderValidator(Validator[TeamBinder]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            schema_service: SchemaService = SchemaService(),
            team_validator: TeamValidator = TeamValidator(),
    ) -> ValidationResult[TeamBinder]:
        """
        # ACTION:
            1.  If the rank fails existence or type checks return the exception in the ValidationResult.
                Else, cast rank into BoardBinder instance binder.
            2.  If either team's has the wrong schema send an exception to the ValidationResult.
            3.  The tests passed. Send the binder in the ValidationResult.
        # PARAMETERS:
            *   rank (Any)
            *   schema_service (SchemaService)
            *   team_service (TeamService)
        # RETURNS:
            *   ValidationResult[BoardBinder] containing either:
                    - On success:   BoardBinder in the payload.
                    - On failure:   Exception.
        Raises:
            *   TypeError
            *   TeamBinderNullException
            *   WhiteTeamHasWrongSchemaException
            *   BlackTeamHasWrongSchemaException
            *   TeamBinderValidationException
        """
        method = "TeamBinderValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationException(
                    msg=f"{method}: {TeamBinderValidationException.MSG}",
                    ex=TeamBinderNullException(f"{method}: {TeamBinderNullException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, TeamBinder):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationException(
                    msg=f"{method}: {TeamBinderValidationException.MSG}",
                    ex=TypeError(f"{method}: Expected BoardBinder, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast the candidate into a BoardBinder for additional tests ---#
        binder = cast(TeamBinder, candidate)
        
        # Handle the case that, the white team does not pass a validation check.
        white_team_validation_result = team_validator.validate(binder.white_team)
        if white_team_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationException(
                    msg=f"{method}: {TeamBinderValidationException.MSG}",
                    ex=white_team_validation_result.exception
                )
            )
        # Handle the case that, the black team does not pass a validation check.
        black_team_validation_result = team_validator.validate(binder.black_team)
        if black_team_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationException(
                    msg=f"{method}: {TeamBinderValidationException.MSG}",
                    ex=black_team_validation_result.exception
                )
            )
        # Handle the case that, the white team does not have a white schema.
        if binder.white_team.schema != schema_service.schema.WHITE:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationException(
                    msg=f"{method}: {TeamBinderValidationException.MSG}",
                    ex=WhiteTeamHasWrongSchemaException(
                        f"{method}: {WhiteTeamHasWrongSchemaException.MSG}"
                    )
                )
            )
        # Handle the case that, the black team does not have a black schema.
        if binder.black_team.schema != schema_service.schema.BLACK:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamBinderValidationException(
                    msg=f"{method}: {TeamBinderValidationException.MSG}",
                    ex=BlackTeamHasWrongSchemaException(
                        f"{method}: {BlackTeamHasWrongSchemaException.MSG}"
                    )
                )
            )
        # On certification successes send the team instance in the ValidationResult.
        ValidationResult.success(payload=binder)