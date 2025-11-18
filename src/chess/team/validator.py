# src/chess/team/validator.py

"""
Module: chess.team.validator
Author: Banji Lawal
Created: 2025-09-11
"""

from typing import cast, Any

from chess.team import InvalidTeamException, Team
from chess.agent import PlayerAgentService
from chess.system import IdentityService, LoggingLevelRouter, Validator, ValidationResult


class TeamValidator(Validator[Team]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    Verifies a candidate is an instance of Team, that meets integrity requirements, before 
    the candidate is used.

    # PROVIDES:
    ValidationResult[Team] containing either:
        - On success: Team in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    No attributes
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Team]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check if candidate is a Team. If so casyt it.
        3.  Check id safety with IdentityService
        4.  Verify schema's correctness with TeamSchemaValidator.
        5.  Check agent safety with PlayerAgentService.
        6.  If any check fails, return the exception inside a ValidationResult.
        7.  If all pass return the Team object in a ValidationResult

        # PARAMETERS:
            *   candidate (Any):                            Object to validate as a Team object.
            
            *   identity_service (IdentityService):         Validates id safety
            
            *   agent_service (PlayerAgentService):         Validares agnent if candidate is a Team .
            
            *   schema_validator (TeamSchemaValidator):     Validates Schema instance's correctness.

        # Returns:
        ValidationResult[Team] containing either:
            - On success:   Team in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullTeamException
            *   InvalidTeamException
        """
        method = "TeamValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamException(f"{method}: {NullTeamException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Team):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Team, got {type(candidate).__name__} instead.")
                )
            
            team = cast(Team, candidate)
            
            id_validation = id_service.validate_id(team.id)
            if not id_validation.is_success():
                return ValidationResult.failure(id_validation.exception)
            
            schema_validation = schema_validation.validate(team.schema)
            if schema_validation.is_failure():
                return ValidationResult.failure(schema_validation.exception)
            
            agent_validation = agent_service.validate(agent)
            if agent_validation.is_failure():
                return ValidationResult.failure(agent_validation.exception)
            
            if team agent_service.found_team(team) is None:
                return ValidationResult.failure(
                    TeamNotRegisterdWithAgentException(f"{method}: {TeamNotRegisterdWithAgentException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(team)
        
        except Exception as ex:
            return ValidationResult.failure(InvalidTeamException(f"{method}: {InvalidTeamException.DEFAULT_MESSAGE}", ex))