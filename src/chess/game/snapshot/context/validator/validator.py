# src/chess/game/snapshot/context/validator/validator.py

"""
Module: chess.game.snapshot.context.validator.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, cast

from chess.team import TeamService
from chess.agent import PlayerAgentService
from chess.system import LoggingLevelRouter, NumberValidator, ValidationResult, Validator
from chess.game import (
    GameSnapshotContext, InvalidGameSnapshotContextException, NoGameSnapshotContextFlagException,
    NullGameSnapshotContextException, TooManyGameSnapshotContextFlagsException
)


class GameSnapshotContextValidator(Validator[GameSnapshotContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1. Verify a candidate is an GameSnapshotContext object's safety before a client uses it.

    # PARENT:
        *   Validator

    # PROVIDES:
        *   GameSnapshotContextValidator.validate -> ValidationResult[GameSnapshotContext]

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
            agent_service: PlayerAgentService = PlayerAgentService(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> ValidationResult[GameSnapshotContext]:
        """
        # Action:
            1.  Confirm that only one in the (id, player_agent, team , arena) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3.  If any check fais return a ValidationResult containing the exception raised by the failure.
            4.  On success send the verified GameSnapshotContext in a ValidationResult.

        # Parameters:
        Only one these must be provided:
            *   timestamp (Optional[int])
            *   player_agent (Optional[PlayerAgent])
            *   team (Optional[Team])

        These Parameters must be provided:
            *   agent_service (PlayerAgentService)
            *   number_validator (NumberValidator)

        # Returns:
        ValidationResult[GameSnapshotContext] containing either:
            - On success: GameSnapshotContext in the payload.
            - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullGameSnapshotContextException
            *   NoGameSnapshotContextFlagException
            *   TooManyGameSnapshotContextFlagsException
            *   InvalidGameSnapshotContextException
        """
        method = "GameSnapshotContextValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullGameSnapshotContextException(f"{method}: {NullGameSnapshotContextException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not an GameSnapshotContext validation has failed.
            if not isinstance(candidate, GameSnapshotContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected GameSnapshotContext, got {type(candidate).__name__} instead.")
                )
            # Once the two existence checks are passed candidate can be cast to an GameSnapshotContext
            # For additional checks.
            context = cast(GameSnapshotContext, candidate)
            
            # Perform the two checks ensuring only one Game attribute value will be used in the searcher.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoGameSnapshotContextFlagException(
                        f"{method}: {NoGameSnapshotContextFlagException.DEFAULT_MESSAGE}"
                    )
                )
            
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    TooManyGameSnapshotContextFlagsException(
                        f"{method}: {TooManyGameSnapshotContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # Certify the context if search is going to be by the snapshot's timestamp
            if context.timestamp is not None:
                validation = number_validator.validate(candidate=context.timestamp)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On validation success return the search_by_game_id context.
                return ValidationResult.success(context)
            
            # Certify the context if search is going to be by the an arena team's player player_agent.
            if context.agent is not None:
                validation = agent_service.validator.validate(candidate=context.agent)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On validation success return the search_by_arena_team_agent context.
                return ValidationResult.success(context)
            
            # Certify the context if search is going to be by the snapshot's arena team
            if context.team is not None:
                validation = team_service.validator.validate(candidate=context.team)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On validation success return the search_by_arena_team context.
                return ValidationResult.success(context)
        
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an InvalidGameSnapshotContextException. Then send exception chain a ValidationResult.failure.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidGameSnapshotContextException(
                    ex=ex, message=f"{method}: {InvalidGameSnapshotContextException.DEFAULT_MESSAGE}"
                )
            )
