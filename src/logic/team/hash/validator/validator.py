# src/logic/team/hash/validation/validation.py

"""
Module: logic.team.hash.validation.validation
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Any, cast

from logic.schema import SchemaService
from logic.system import LoggingLevelRouter, ValidationProcess
from logic.system.validate.result import ValidationResult
from logic.team import (
    BlackTeamHasWrongSchemaException, TeamHash, TeamHashNullException, TeamHashValidationException,
    TeamValidationProcess, WhiteTeamHasWrongSchemaException
)


class TeamHashValidationProcess(ValidationProcess[TeamHash]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            schema_service: SchemaService = SchemaService(),
            team_validator: TeamValidationProcess = TeamValidationProcess(),
    ) -> ValidationResult[TeamHash]:
        """
        # ACTION:
            1.  If the candidate fails existence or type checks return the exception in the ValidationResult.
                Else, cast candidate into TeamHash instance hash.
            2.  If either team's has the wrong schema send an exception to the ValidationResult.
            3.  The tests passed. Send the hash in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
            *   schema_service (SchemaService)
            *   team_service (TeamService)
        # RETURNS:
            *   ValidationResult[TeamHash] containing either:
                    - On success:   TeamHash in the payload.
                    - On failure:   Exception.
        Raises:
            *   TypeError
            *   TeamHashNullException
            *   WhiteTeamHasWrongSchemaException
            *   BlackTeamHasWrongSchemaException
            *   TeamHashValidationException
        """
        method = "TeamHashValidationProcess.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamHashValidationException(
                    msg=f"{method}: {TeamHashValidationException.MSG}",
                    ex=TeamHashNullException(f"{method}: {TeamHashNullException.MSG}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, TeamHash):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamHashValidationException(
                    msg=f"{method}: {TeamHashValidationException.MSG}",
                    ex=TypeError(f"{method}: Expected TeamHash, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast the candidate to a TeamHash for additional tests ---#
        hash = cast(TeamHash, candidate)
        
        # Handle the case that, the white team is not certified as safe.
        white_team_validation_result = team_validator.execute(hash.white_team)
        if white_team_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamHashValidationException(
                    msg=f"{method}: {TeamHashValidationException.MSG}",
                    ex=white_team_validation_result.exception
                )
            )
        # Handle the case that, the black team is not certified as safe.
        black_team_validation_result = team_validator.execute(hash.black_team)
        if black_team_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamHashValidationException(
                    msg=f"{method}: {TeamHashValidationException.MSG}",
                    ex=black_team_validation_result.exception
                )
            )
        # Handle the case that, the white team does not have a white schema.
        if hash.white_team.schema != schema_service.schema.WHITE:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamHashValidationException(
                    msg=f"{method}: {TeamHashValidationException.MSG}",
                    ex=WhiteTeamHasWrongSchemaException(
                        f"{method}: {WhiteTeamHasWrongSchemaException.MSG}"
                    )
                )
            )
        # Handle the case that, the black team does not have a black schema.
        if hash.black_team.schema != schema_service.schema.BLACK:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamHashValidationException(
                    msg=f"{method}: {TeamHashValidationException.MSG}",
                    ex=BlackTeamHasWrongSchemaException(
                        f"{method}: {BlackTeamHasWrongSchemaException.MSG}"
                    )
                )
            )
        # On certification successes send the team instance in the ValidationResult.
        ValidationResult.success(payload=hash)