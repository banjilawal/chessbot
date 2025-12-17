# src/chess/team/context/validator/validator.py

"""
Module: chess.team.context.validator.validator
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Any, cast

from chess.agent import PlayerAgentService
from chess.arena import ArenaService
from chess.system import GameColorValidator, IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.team import (
    InvalidTeamContextException, NoTeamContextFlagsException, NullTeamContextException, TeamContext, Team,
    TeamValidator, TooManyTeamContextFlagsException
)


class TeamContextValidator(Validator[TeamContext]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

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
                        team_schema: Team = Team,
                        agent_certifier: PlayerAgentService = PlayerAgentService(),
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
            arena_service: ArenaService = ArenaService(),
            agent_service: PlayerAgentService = PlayerAgentService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> ValidationResult[TeamContext]:
        """
        # Action:
        1.  Confirm that only one in the (id, designation, player_agent, arena, color) tuple is not null.
        2.  Certify the not-null attribute is safe using the appropriate service's validator.
        3.  If any check fais return a ValidationResult containing the exception raised by the failure.
        4.  On success Build an TeamContext are return in a ValidationResult.

        # Parameters:
            *   candidate (Any)
            *   color_validator (ColorValidator)
            *   player_agent_service (PlayerAgentService)
            *   arena_service (ArenaService)
            *   identity_service (IdentityService)

        # Returns:
        ValidationResult[TeamContext] containing either:
            - On success: TeamContext in the payload.
            - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullTeamContextException
            *   NoTeamContextFlagException
            *   TooManyTeamContextFlagsException
            *   InvalidTeamContextException
        """
        method = "TeamContextValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamContextException(f"{method}: {NullTeamContextException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not an TeamContext validation has failed.
            if not isinstance(candidate, TeamContext):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected TeamContext, got {type(candidate).__name__} instead.")
                )
            
            # Once existence and type checks are passed, cast the candidate to Team and run structure tests.
            context = cast(TeamContext, candidate)
            
            # Handle the case of searching with no attribute-value.
            if len(context.to_dict()) == 0:
                return ValidationResult.failure(
                    NoTeamContextFlagsException(f"{method}: {NoTeamContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Handle the case of too many attributes being used in a search.
            if len(context.to_dict()) > 1:
                return ValidationResult.failure(
                    TooManyTeamContextFlagsException(
                        f"{method}: {TooManyTeamContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # When structure tests are passed certify whichever search value was provided.
            
            # Certification for the search-by-id target.
            if context.id is not None:
                validation = identity_service.validate_id(candidate=context.id)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the team_id_context in a ValidationResult.
                return ValidationResult.success(payload=context)
            
            # Certification for the search-by-designation target.
            if context.name is not None:
                validation = identity_service.validate_name(candidate=context.name)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the team_name_context in a ValidationResult.
                return ValidationResult.success(payload=context)
            
            # Certification for the search-by-player_agent target.
            if context.player_agent is not None:
                validation = agent_service.validator.validate(candidate=context.player_agent)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the team_agent_context in a ValidationResult.
                return ValidationResult.success(payload=context)
            
            # Certification for the search-by-arena target.
            if context.arena is not None:
                validation = arena_service.validator.validate(candidate=context.arena)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the team_arena_context in a ValidationResult.
                return ValidationResult.success(payload=context)
            
            # Certification for the search-by-color target.
            if context.color is not None:
                validation = color_validator.validate(candidate=context.color)
                if validation.is_failure:
                    return ValidationResult.failure(validation.exception)
                # On certification success return the team_color_context in a ValidationResult.
                return ValidationResult.success(payload=context)
            
        # Finally, if there is an unhandled exception Wrap a TeamBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamContextException(
                    ex=ex, message=f"{method}: {InvalidTeamContextException.DEFAULT_MESSAGE}"
                )
            )