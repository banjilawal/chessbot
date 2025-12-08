# src/chess/team/context/validator/validator.py

"""
Module: chess.team.context.validator.validator
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Any, cast

from chess.agent import AgentService
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.team import (
    InvalidTeamContextException, NoTeamContextFlagsException, NullTeamContextException, TeamContext, TeamSchema,
    TeamSchemaValidator, TooManyTeamContextFlagsException
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
    
    # CONSTRUCTOR:
    Default Constructor
    
    # CLASS METHODS:
        ## Validate signature:
                validate(
                        candidate: Any,
                        schema: TeamSchema = TeamSchema,
                        agent_certifier: AgentService = AgentService(),
                        identity_service: IdentityService = IdentityService(),
                ) -> ValidationResult[TeamContext]:
                
    # INSTANCE METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            schema: TeamSchema = TeamSchema,
            agent_service: AgentService = AgentService(),
            idservice: IdentityService = IdentityService(),
            schema_validator: TeamSchemaValidator = TeamSchemaValidator(),
    ) -> ValidationResult[TeamContext]:
        """
        # ACTION:
        1.  Check candidate is not null.
        2.  Check if candidate is a TeamContext. If so cast it.
        3.  Verify only one flag is set.
        4.  For whichever of the flag is set certify its correctness with either validators in:
            AgentService or IdentityService.
        5.  If any check fails, return the exception inside a ValidationResult.
        7.  If all pass return the TeamContext object in a ValidationResult

        # PARAMETERS:
            *   candidate (Any)
            *   identity_service (IdentityService):
            *   agent_certifier (PlayerAgentService):
            *   schema (TeamSchema)

        # Returns:
        ValidationResult[TeamContext] containing either:
            - On success:   TeamContext in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullTeamContextException
            *   InvalidTeamContextException
        """
        method = "TeamContextValidator.validate"
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamContextException(f"{method}: {NullTeamContextException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, TeamContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected TeamContext, got {type(candidate).__name__} instead.")
                )
            # After not-null and type checks have passed cast te TeamContext.
            context = cast(TeamContext, candidate)
            # Check if no flags were set.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoTeamContextFlagsException(f"{method}: {NoTeamContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Check if more than one flag is set.
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    TooManyTeamContextFlagsException(
                        f"{method}: {TooManyTeamContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # If no errors are detected pick the flag whose value is not for processing.
            if context.id is not None:
                validation = idservice.validate_id(candidate=context.id)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(payload=context)
            
            if context.name is not None:
                validation = idservice.validate_name(candidate=context.name)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(payload=context)
            
            if context.agent is not None:
                validation = agent_service.item_validator.validate(candidate=context.agent)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(payload=context)
            
            if context.color is not None:
                validation = schema_validator.verify_color_in_schema(candidate=context.color)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
        # Finally, if there is an unhandled exception Wrap a TeamBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamContextException(
                    ex=ex, message=f"{method}: {InvalidTeamContextException.DEFAULT_MESSAGE}"
                )
            )
