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
        """
        # Action:
            1.  Confirm that only one in the (id, name, team, game, variety) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate service and validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success Build an AgentContext are return in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   name (Optional[str])
            *   team (Optional[Team])
            *   game (Optional[Game])
            *   variety (Optional[AgentVariety])

        These Parameters must be provided:
            *   team_service (TeamService)
            *   game_service (GameService)
            *   identity_service (IdentityService)

        # Returns:
          BuildResult[AgentContext] containing either:
                - On success: AgentContext in the payload.
                - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullAgentContextException
            *   NoAgentContextFlagException
            *   TooManyAgentContextFlagsException
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
            # Once the two existence checks are passed candidate can be cast to an AgentContext
            # For additional checks.
            context = cast(AgentContext, candidate)
            
            # Perform the two checks ensuring only one Agent attribute value will be used in the search.
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
            # Which ever attribute value is not null should be certified safe by the appropriate validator.
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
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an InvalidAgentContextException. Then send exception chain a ValidationResult.failure.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidAgentContextException(
                    ex=ex, message=f"{method}: {InvalidAgentContextException.DEFAULT_MESSAGE}"
                )
            )