# src/chess/game/context/validator/validator.py

"""
Module: chess.game.context.validator.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Any, cast


from chess.agent import AgentService
from chess.system import LoggingLevelRouter, Validator, ValidationResult, IdentityService
from chess.game import (
    GameContext, InvalidGameContextException, NoGameContextFlagException, NullGameContextException,
    TooManyGameContextFlagsException
)


class GameContextValidator(Validator[GameContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a GameContext instance is certified safe, reliable and consistent before use.
    2.  Provide the verification customer an exception detailing the contract violation if integrity assurance fails.

    # PARENT:
        *   Validator

    # PROVIDES:
        * GameContextValidator

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
            1.  Confirm that only one in the (id, agent) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success send the verified GameContext in a ValidationResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   agent (Optional[Agent])

        These Parameters must be provided:
            *   agent_service (AgentService)
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
            # Null candidates are not allowed.
            if candidate is None:
                return ValidationResult.failure(
                    NullGameContextException(f"{method}: {NullGameContextException.DEFAULT_MESSAGE}")
                )
            # Ensure the candidate is a GameContext
            if not isinstance(candidate, GameContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected GameContext, got {type(candidate).__name__} instead.")
                )
            
            # After existence and type checks cast the candidate for further processing.
            context = cast(GameContext, candidate)
            
            # Make sure a search target exists in the context. Cannot perform a search without an
            # property-value pair.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoGameContextFlagException(f"{method}: {NoGameContextFlagException.DEFAULT_MESSAGE}")
                )
            # Return an error if more than one property value pair exists in the context.
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    TooManyGameContextFlagsException(
                        f"{method}: {TooManyGameContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            
            # Verify the id flag if its enabled.
            if context.id is not None:
                validation = identity_service.validate_id(candidate=context.id)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                # On validation success return the id_game_context in a ValidationResult.
                return ValidationResult.success(context)
            
            # Verify the id flag if its enabled.
            if context.agent is not None:
                validation = agent_service.validator.validate(candidate=context.agent)
                if validation.is_failure():
                    return ValidationResult.failure(validation.exception)
                # On validation success return the agent_game_context in a ValidationResult.
                return ValidationResult.success(context)
            
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an InvalidGameContextException. Then send exception chain a ValidationResult.failure.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidGameContextException(
                    ex=ex, message=f"{method}: {InvalidGameContextException.DEFAULT_MESSAGE}"
                )
            )
