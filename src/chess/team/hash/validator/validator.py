# src/chess/team/hash/validator/validator.py

"""
Module: chess.team.hash.validator.validator
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Any, cast

from chess.schema import SchemaService
from chess.system import LoggingLevelRouter, Validator
from chess.system.validate.result import ValidationResult
from chess.team import (
    BlackTeamHasWrongSchemaException, TeamHash, TeamHashNullException, TeamHashValidationFailedException, TeamValidator,
    WhiteTeamHasWrongSchemaException
)


class TeamHashValidator(Validator[TeamHash]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            schema_service: SchemaService = SchemaService(),
            team_validator: TeamValidator = TeamValidator(),
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
        # RAISES:
            *   TypeError
            *   TeamHashNullException
            *   WhiteTeamHasWrongSchemaException
            *   BlackTeamHasWrongSchemaException
            *   TeamHashValidationFailedException
        """
        method = "TeamHashValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamHashValidationFailedException(
                    message=f"{method}: {TeamHashValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TeamHashNullException(f"{method}: {TeamHashNullException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, TeamHash):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamHashValidationFailedException(
                    message=f"{method}: {TeamHashValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected TeamHash, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast the candidate to a TeamHash for additional tests ---#
        hash = cast(TeamHash, candidate)
        
        # Handle the case that the white team is not certified as safe.
        white_team_validation_result = team_validator.validate(hash.white_team)
        if white_team_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamHashValidationFailedException(
                    message=f"{method}: {TeamHashValidationFailedException.DEFAULT_MESSAGE}",
                    ex=white_team_validation_result.exception
                )
            )
        # Handle the case that the black team is not certified as safe.
        black_team_validation_result = team_validator.validate(hash.black_team)
        if black_team_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamHashValidationFailedException(
                    message=f"{method}: {TeamHashValidationFailedException.DEFAULT_MESSAGE}",
                    ex=black_team_validation_result.exception
                )
            )
        # Handle the case that the white team does not have a white schema.
        if hash.white_team.schema != schema_service.schema.WHITE:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamHashValidationFailedException(
                    message=f"{method}: {TeamHashValidationFailedException.DEFAULT_MESSAGE}",
                    ex=WhiteTeamHasWrongSchemaException(
                        f"{method}: {WhiteTeamHasWrongSchemaException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the black team does not have a black schema.
        if hash.black_team.schema != schema_service.schema.BLACK:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamHashValidationFailedException(
                    message=f"{method}: {TeamHashValidationFailedException.DEFAULT_MESSAGE}",
                    ex=BlackTeamHasWrongSchemaException(
                        f"{method}: {BlackTeamHasWrongSchemaException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # On certification successes send the team instance in the ValidationResult.
        ValidationResult.success(payload=hash)