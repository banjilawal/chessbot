# src/chess/game/context/validator/validator.py

"""
Module: chess.game.context.validator.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Any, cast

from chess.game import GameService
from chess.agent import AgentService
from chess.system import LoggingLevelRouter, Validator, ValidationResult, IdentityService
from chess.game import (
    GameContext, GameVariety, InvalidGameContextException, NoGameContextFlagException, NullGameContextException,
    TooManyGameContextFlagsException
)


class GameContextValidator(Validator[GameContext]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    1. Verify a candidate is an GameContext object's safety before a client uses it.

    # PARENT
        *   Validator

    # PROVIDES:
    ValidationResult[GameContext] containing either:
        - On success: GameContext in the payload.
        - On failure: Exception.

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
            agent_service: AgentService = AgentService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[GameContext]:
        """
        # Action:
            1.  Confirm that only one in the (id, name, agent, game, game_variety) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success Build an GameContext are return in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   name (Optional[str])
            *   agent (Optional[Agent])
            *   game (Optional[Game])
            *   game_variety (Optional[GameVariety])

        These Parameters must be provided:
            *   agent_service (AgentService)
            *   game_service (GameService)
            *   identity_service (IdentityService)

        # Returns:
          BuildResult[GameContext] containing either:
                - On success: GameContext in the payload.
                - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullGameContextException
            *   NoGameContextFlagException
            *   TooManyGameContextFlagsException
            *   InvalidGameContextException
        """
        method = "GameContextValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullGameContextException(f"{method}: {NullGameContextException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not an GameContext validation has failed.
            if not isinstance(candidate, GameContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected GameContext, got {type(candidate).__name__} instead.")
                )
            # Once the two existence checks are passed candidate can be cast to an GameContext
            # For additional checks.
            context = cast(GameContext, candidate)
            
            # Perform the two checks ensuring only one Game attribute value will be used in the searcher.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoGameContextFlagException(f"{method}: {NoGameContextFlagException.DEFAULT_MESSAGE}")
                )
            
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    TooManyGameContextFlagsException(
                        f"{method}: {TooManyGameContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # Which ever attribute value is not null should be certified safe by the appropriate validator.
            if context.id is not None:
                validation = identity_service.validate_id(candidate=context.id)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
            if context.agent is not None:
                validation = agent_service.item_validator.validate(candidate=context.agent)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                return ValidationResult.success(context)
            
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an InvalidGameContextException. Then send exception chain a ValidationResult.failure.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidGameContextException(
                    ex=ex, message=f"{method}: {InvalidGameContextException.DEFAULT_MESSAGE}"
                )
            )
