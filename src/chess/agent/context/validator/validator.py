# src/chess/agent/context/validator/validator.py

"""
Module: chess.agent.context.validator.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Any, cast

from chess.game import GameService
from chess.team import TeamService
from chess.system import LoggingLevelRouter, Validator, ValidationResult, IdentityService
from chess.agent import (
    AgentContext, AgentVariety, InvalidAgentContextException, NoAgentContextFlagException, NullAgentContextException,
    TooManyAgentContextFlagsException
)


class AgentContextValidator(Validator[AgentContext]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    1. Verify a candidate is an AgentContext object's safety before a client uses it.

    # PROVIDES:
      ValidationResult[AgentContext] containing either:
            - On success: AgentContext in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            team_service: TeamService = TeamService(),
            game_service: GameService = GameService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[AgentContext]:
        """"""
        method = "AgentContextValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullAgentContextException(f"{method}: {NullAgentContextException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, AgentContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected AgentContext, got {type(candidate).__name__} instead.")
                )
            
            context = cast(AgentContext, candidate)
            
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoAgentContextFlagException(f"{method}: {NoAgentContextFlagException.DEFAULT_MESSAGE}")
                )
            
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    TooManyAgentContextFlagsException(
                        f"{method}: {TooManyAgentContextFlagsException.DEFAULT_MESSAGE}"
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
                validation = team_service.item_validator.validate(candidate=context.name)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.game is not None:
                validation = game_service.item_validator.validate(candidate=context.name)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.variety is not None:
                if context.variety not in [AgentVariety.HUMAN_AGENT, AgentVariety.MACHINE_AGENT]:
                    return ValidationResult.failure(
                        TypeError(f"{method}: Expected AgentType, got {type(candidate).__name__} instead.")
                    )
                return ValidationResult.success(context)
            
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentContextException(
                    ex=ex,
                    message=f"{method}: {InvalidAgentContextException.DEFAULT_MESSAGE}"
                )
            )
        
