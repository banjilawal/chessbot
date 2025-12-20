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
    AgentContext, AgentVariety, ExcessiveAgentContextFlagsException, InvalidAgentContextException,
    NullAgentContextException, ZeroAgentContextFlagsException
)


class AgentContextValidator(Validator[AgentContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure an AgentContext instance is certified safe, reliable and consistent before use.
    2.  Provide the verification customer an exception detailing the contract violation if integrity assurance fails.

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
        # Action:
        1.  Confirm that only one in the (id, designation, team, game, agent_variety) tuple is not null.
        2.  Certify the not-null attribute is safe using the appropriate service's number_bounds_validator.
        3.  If any check fais return a ValidationResult containing the exception raised by the failure.
        4.  On success Build an AgentContext are return in a ValidationResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   designation (Optional[str])
            *   team (Optional[Team])
            *   game (Optional[Game])
            *   agent_variety (Optional[AgentVariety])

        These Parameters must be provided. By default, they are automatically set:
            *   team_service (TeamService)
            *   game_service (GameService)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[AgentContext] containing either:
            - On success: AgentContext in the payload.
            - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullAgentContextException
            *   NoAgentContextFlagException
            *   ExcessiveAgentContextFlagsException
            *   InvalidAgentContextException
        """
        method = "AgentContextValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullAgentContextException(f"{method}: {NullAgentContextException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not an AgentContext validation has failed.
            if not isinstance(candidate, AgentContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected AgentContext, got {type(candidate).__name__} instead.")
                )
            
            # Cast to an AgentContext for additional processing.
            context = cast(AgentContext, candidate)
            
            # Perform the two checks ensuring only one PlayerAgent attribute value will be used in the searcher.
            # Handle the case of searching with no attribute-value.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroAgentContextFlagsException(f"{method}: {ZeroAgentContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Handle the case of too many attributes being used in a search.
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    ExcessiveAgentContextFlagsException(
                        f"{method}: {ExcessiveAgentContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # Which ever attribute value is not null should be certified safe by the appropriate number_bounds_validator.
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
                        TypeError(f"{method}: Expected AgentType, got {type(candidate).__name__} instead.")
                    )
                return ValidationResult.success(context)
            
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an InvalidAgentContextException. Then send the exception-chain in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentContextException(
                    ex=ex, message=f"{method}: {InvalidAgentContextException.DEFAULT_MESSAGE}"
                )
            )
