# src/chess/team/context/validator/validator.py

"""
Module: chess.team.context.validator.validator
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Any, cast

from chess.agent import AgentService
from chess.system import BuildResult, IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.team import (
    InvalidTeamContextException, NoTeamContextFlagsException, NullTeamContextException, TeamContext,
    TeamContextBuildFailedException, TeamSchema, TooManyTeamContextFlagsException
)


class TeamContextValidator(Validator[TeamContext]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    Verifies a candidate is an instance of TeamContext, that meets integrity requirements, before
    the candidate is used.

    # PROVIDES:
    ValidationResult[TeamContext] containing either:
        - On success: Team in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    No attributes
    """
    @classmethod
    def validate(
            cls,
            candidate: Any,
            schema: TeamSchema = TeamSchema,
            agent_service: AgentService = AgentService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[TeamContext]:
        """"""
        method = "TeamContextValidator.validate"
            
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamContextException(f"{method}: {NullTeamContextException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, TeamContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected TeamContext, got {type(candidate).__name__} instead.")
                )
            
            context = cast(TeamContext, candidate)
            
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoTeamContextFlagsException(f"{method}: {NoTeamContextFlagsException.DEFAULT_MESSAGE}")
                )
            
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    TooManyTeamContextFlagsException(f"{method}: {TooManyTeamContextFlagsException.DEFAULT_MESSAGE}")
                )
            
            if context.id is not None:
                validation = identity_service.validate_id(candidate=context.id)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.name is not None:
                validation = identity_service.validate_name(candidate=context.name)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.agent is not None:
                validation = agent_service.validator.validate(candidate=context.agent)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.succes(context)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamContextException(ex=ex, message=f"{method}: {InvalidTeamContextException.DEFAULT_MESSAGE}")
            )