# src/chess/agent/validator/validator.py

"""
Module: chess.agent.validator.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Any, cast

from chess.game import GameService
from chess.team import TeamService
from chess.system import LoggingLevelRouter, Validator, ValidationResult, IdentityService
from chess.agent import (
    AgentContext,  ExcessiveAgentContextFlagsException, InvalidAgentContextException,
    NullAgentContextException, ZeroAgentContextFlagsException
)


class AgentContextValidator(Validator[AgentContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure an AgentContext instance is certified safe, reliable and consistent before use.
    2.  If a candidate fails a safety test, the validator sends an exception in a ValidationResult.
    
    # PARENT:
        *   Validator

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
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
        """
        # ACTION:
            1.  If the candidate passes existence and type checks cast into a AgentContext for
                additional integrity tests. Else return an exception in the ValidationResult.
            2.  If one-and-only-one AgentContext attribute-value-tuple is enabled goto the integrity
                check. Else, return an exception in the ValidationResult.
            3.  Route to the appropriate validation subflow with the attribute as the routing key.
            4.  If the validation subflow certifies the map tuple return it in the validation result.
                Else, send the exception in the ValidationResult.

        # PARAMETERS:
            *   candidate (Any)
            *   team_service (TeamService)
            *   game_service (GameService)
            *   identity_service (IdentityService)

        # RETURNS:
        ValidationResult[AgentContext] containing either:
            - On success: AgentContext in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullAgentContextException
            *   NoAgentContextFlagException
            *   ExcessiveAgentContextFlagsException
            *   InvalidAgentContextException
        """
        method = "AgentContextValidator.validate"
        try:
            # Handle the nonexistence case.
            if candidate is None:
                return ValidationResult.failure(
                    NullAgentContextException(f"{method}: {NullAgentContextException.DEFAULT_MESSAGE}")
                )
            # Handle the wrong class case.
            if not isinstance(candidate, AgentContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected AgentContext instance, got {type(candidate).__name__} instead.")
                )
            
            # After existence and type checks are successful cast the candidate to an AgentContext
            # for additional tests.
            context = cast(AgentContext, candidate)
            
            # Handle the no map flag enabled case.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroAgentContextFlagsException(f"{method}: {ZeroAgentContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Handle the excessive map flags case.
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    ExcessiveAgentContextFlagsException(
                        f"{method}: {ExcessiveAgentContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            
            # Using the tuple's attribute as an address, route to appropriate validation subflow.
            
            # Which ever attribute value is not null should be certified safe by the appropriate validator.
            if context.id is not None:
                validation = identity_service.validate_id(candidate=context.id)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.name is not None:
                validation = identity_service.validate_name(candidate=context.name)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.team is not None:
                validation = team_service.validator.validate(candidate=context.team)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.game is not None:
                validation = game_service.validator.validate(candidate=context.game)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.variety is not None:
                if context.variety not in [AgentVariety.HUMAN_AGENT, AgentVariety.MACHINE_AGENT]:
                    return ValidationResult.failure(
                        TypeError(f"{method}: Expected AgentType instance, got {type(candidate).__name__} instead.")
                    )
                return ValidationResult.success(context)
        
        # Finally, catch any missed exception, wrap an InvalidAgentContextException around it then, return
        # the exception-chain inside the ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentContextException(
                    ex=ex, message=f"{method}: {InvalidAgentContextException.DEFAULT_MESSAGE}"
                )
            )
