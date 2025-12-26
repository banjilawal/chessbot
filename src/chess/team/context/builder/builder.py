# src/chess/team/builder/builder.py

"""
Module: chess.team.builder.builder
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional


from chess.arena import Arena, ArenaService
from chess.agent import PlayerAgent, AgentService
from chess.system import (
    Builder, BuildResult, UnhandledRouteException, GameColor, GameColorValidator,
    IdentityService, LoggingLevelRouter
)
from chess.team import (
    NoTeamContextFlagException, TeamContext, TeamContextBuildFailedException, ExcessiveTeamContextFlagsException,
    TeamContextBuildRouteException
)


class TeamContextBuilder(Builder[TeamContext]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce TeamContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of TeamContext instances that can be used safely by the client.
    3.  Ensure params for TeamContext creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
        *   Builder

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            arena: Optional[Arena] = None,
            owner: Optional[PlayerAgent] = None,
            color: Optional[GameColor] = None,
            arena_service: ArenaService = ArenaService(),
            owner_service: AgentService = AgentService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[TeamContext]:
        """
        # Action:
            1.  Confirm that only one in the tuple (id, designation, owner, color, team_schema), is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a TeamContext and send in a BuildResult. Else, return an exception
                in the BuildResult.

        # Parameters:
            Only one these must be provided:
                *   id (Optional[int])
                *   designation (Optional[int])
                8   arena (Optional[Arena])
                *   owner (Optional[PlayerAgent])
                *   color (Optional[ArenaColor])
    
            These Parameters must be provided:
                *   arena_service (ArenaService)
                *   agent_certifier (AgentService)
                *   identity_service (IdentityService)
                *   schema_validator (TeamSchemaValidator)

        # Returns:
        BuildResult[TeamContext] containing either:
            - On success: TeamContext in the payload.
            - On failure: Exception.

        # Raises:
            *   ZeroTeamContextFlagsException
            *   TeamContextBuildFailedException
            *   ExcessiveTeamContextFlagsException
        """
        method = "PieceSearchContextBuilder.builder"
        
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, name, arena, owner, color]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which Teams match the target.
            if param_count == 0:
                return BuildResult.failure(
                    TeamContextBuildFailedException(
                        message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                        ex=NoTeamContextFlagException(f"{method}:  {NoTeamContextFlagException.DEFAULT_MESSAGE}")
                    )
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    TeamContextBuildFailedException(
                        message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                        ex=ExcessiveTeamContextFlagsException(f"{method}: {ExcessiveTeamContextFlagsException}")
                    )
                )
            # After verifying only one Team attribute-value-tuple is enabled, validate it.
            
            # Build the id TeamContext if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(candidate=id)
                if validation.is_failure:
                    return BuildResult.failure(
                        TeamContextBuildFailedException(
                            message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                            ex=validation.exception
                        )
                    )
                # On validation success return an id_TeamContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(id=validation.id))
            
            # Build the owner TeamContext if its flag is enabled.
            if owner is not None:
                validation = owner_service.validator.validate(candidate=owner)
                if validation.is_failure:
                    return BuildResult.failure(
                        TeamContextBuildFailedException(
                            message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                            ex=validation.exception
                        )
                    )
                # On validation success return a owner.TeamContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(owner=validation.payload))
            
            # Build the arena TeamContext if its flag is enabled.
            if arena is not None:
                validation = arena_service.item_validator.validate(candidate=arena)
                if validation.is_failure:
                    return BuildResult.failure(
                        TeamContextBuildFailedException(
                            message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                            ex=validation.exception
                        )
                    )
                # On validation success return an arena_GameContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(owner=validation.payload))
            
            # Build the color TeamContext if its flag is enabled.
            if color is not None:
                validation = color_validator.validate(candidate=color)
                if validation.is_failure:
                    return BuildResult.failure(
                        TeamContextBuildFailedException(
                            message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                            ex=validation.exception
                        )
                    )
                # On validation success return a color_GameContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(color=validation.payload))
            
        return BuildResult.failure(
            TeamContextBuildFailedException(
                message=f"{method}: {TeamContextBuildFailedException.ERROR_CODE}",
                ex=TeamContextBuildRouteException(f"{method}: {TeamContextBuildRouteException.DEFAULT_MESSAGE}")
            )
        )