# src/chess/agent/context/validator/validator.py

"""
Module: chess.agent.context.validator.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Any, cast

from chess.team import Team, TeamService
from chess.system import LoggingLevelRouter, Validator, ValidationResult, IdentityService
from chess.agent import (
    AgentType, AgentContext, InvalidAgentContextException, NoAgentContextFlagSetException,
    NullAgentContextException,
    TooManyAgentContextFlagsSetException
)


class AgentContextValidator(Validator[AgentContext]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            team_service: TeamService = TeamService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[AgentContext]:
        """"""
        method = "AgentContextValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullAgentContextException(
                        f"{method}: "
                        f"{NullAgentContextException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, AgentContext):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected AgentContext, got {type(candidate).__name__} instead."
                    )
                )
            
            context = cast(AgentContext, candidate)
            
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoAgentContextFlagSetException(
                        f"{method}: "
                        f"{NoAgentContextFlagSetException.DEFAULT_MESSAGE}"
                    )
                )
            
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    TooManyAgentContextFlagsSetException(
                        F"{method}: "
                        F"{TooManyAgentContextFlagsSetException.DEFAULT_MESSAGE}"
                    )
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
            
            if context.team is not None:
                validation = team_service.validator.validate(candidate=context.team)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.agent_type is not None:
                if context.agent_type not in [AgentType.HUMAN_AGENT, AgentType.MACHINE_AGENT]:
                    return ValidationResult.failure(
                        TypeError(
                            (
                                f"{method}: Expected AgentType, "
                                f"got {type(candidate).__name__} instead."
                            )
                        )
                    )
                return ValidationResult.success(context)
            
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentContextException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{InvalidAgentContextException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
