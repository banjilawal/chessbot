# src/chess/snapshot/validator/validator.py

"""
Module: chess.snapshot.validator.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, cast

from chess.agent import AgentService
from chess.arena import ArenaService
from chess.game import GameService
from chess.snapshot import NullSnapshotContextException, SnapshotContext
from chess.snapshot.context.validator.exception.base import InvalidSnapshotContextException
from chess.snapshot.context.validator.exception.flag.excess import ExcessiveSnapshotContextFlagsException
from chess.snapshot.context.validator.exception.flag.zero import ZeroSnapshotContextFlagsException
from chess.team import TeamService
from chess.system import (
    IdentityService, LoggingLevelRouter, NullException, NumberInBoundsValidator, NumberValidator,
    ValidationResult, Validator
)



class SnapshotContextValidator(Validator[SnapshotContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure an SnapshotContext instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

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
            game_service: GameService = GameService(),
            team_service: TeamService = TeamService(),
            arena_service: ArenaService = ArenaService(),
            player_service: AgentService = AgentService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[SnapshotContext]:
        """
        # ACTION:
            1.  If the candidate passes existence and type checks cast into a SnapshotContext for
                additional integrity tests. Else return an exception in the ValidationResult.
            2.  If one-and-only-one SnapshotContext attribute-value-tuple is enabled goto the integrity
                check. Else, return an exception in the ValidationResult.
            3.  Route to the appropriate validation subflow with the attribute as the routing key.
            4.  If the validation subflow certifies the map tuple return it in the validation result.
                Else, send the exception in the ValidationResult.

        # PARAMETERS:
            *   candidate (Any)
            *   game_service (GameService)
            *   team_service (TeamService)
            *   arena_service (ArenaService)
            *   player_service (AgentService)
            *   identity_service (IdentityService)

        # RETURNS:
        ValidationResult[SnapshotContext] containing either:
            - On success: SnapshotContext in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   NullSnapshotContextException
            *   ZeroSnapshotContextFlagsException
            *   ExcessiveSnapshotContextFlagsException
            *   InvalidSnapshotContextException
        """
        method = "SnapshotContextValidator.validate"
        try:
            # Handle the nonexistence case.
            if candidate is None:
                return ValidationResult.failure(
                    NullSnapshotContextException(f"{method}: {NullSnapshotContextException.DEFAULT_MESSAGE}")
                )
            # Handle the wrong class case.
            if not isinstance(candidate, SnapshotContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected SnapshotContext instance, got {type(candidate).__name__} instead.")
                )
            
            # After existence and type checks are successful cast the candidate to a SnapshotContext
            # for additional tests.
            context = cast(SnapshotContext, candidate)
            
            # Handle the no map flag enabled case.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroSnapshotContextFlagsException(
                        f"{method}: {ZeroSnapshotContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # Handle the excessive map flags case.
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    ExcessiveSnapshotContextFlagsException(
                        f"{method}: {ExcessiveSnapshotContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            
            # Using the tuple's attribute as an address, route to appropriate validation subflow.
            
            # Validation subflow for game SnapshotContexts.
            if context.game is not None:
                validation = game_service.validator.validate(candidate=context.game)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On validation success return the game_SnapshotContext in the validation Result.
                return ValidationResult.success(context)

            # Validation subflow for team SnapshotContexts.
            if context.team is not None:
                validation = team_service.validator.validate(candidate=context.team)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On validation success return the team_SnapshotContext ValidationResult..
                return ValidationResult.success(context)
            
            # Validation subflow for arena SnapshotContexts.
            if context.arena is not None:
                validation = arena_service.validator.validate(candidate=context.arena)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On validation success return the arena_SnapshotContext in the validation Result.
                return ValidationResult.success(context)
            
            # Validation subflow for timestamp SnapshotContexts.
            if context.timestamp is not None:
                validation = identity_service.validate_id(candidate=context.timestamp)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On validation success return the timestamp_SnapshotContext in the ValidationResult.
                return ValidationResult.success(context)
            
            # Validation subflow for exception SnapshotContexts.
            if context.exception is not None:
                if not isinstance(context.exception, Exception):
                    return ValidationResult.failure(NullException(f"{method}: {NullException.DEFAULT_MESSAGE}"))
                # On validation success return the exception_SnapshotContext in the ValidationResult.
                return ValidationResult.success(context)

            # Validation subflow for player SnapshotContexts.
            if context.plyer is not None:
                validation = player_service.validator.validate(candidate=context.player)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On validation success return the player_SnapshotContext in the ValidationResult
                return ValidationResult.success(context)
        
        # Finally, catch any missed exception, wrap an InvalidSnapshotContextException around it then
        # return the exception-chain inside the ValidationResult
        except Exception as ex:
            return ValidationResult.failure(
                InvalidSnapshotContextException(
                    ex=ex, message=f"{method}: {InvalidSnapshotContextException.DEFAULT_MESSAGE}"
                )
            )
