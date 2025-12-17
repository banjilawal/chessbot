# src/chess/team/context/builder/builder.py

"""
Module: chess.team.context.builder.builder
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.agent import PlayerAgent, PlayerAgentService
from chess.arena import Arena, ArenaService
from chess.system import Builder, BuildResult, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter
from chess.team import (
    NoTeamContextFlagsException, TeamContext, TeamContextBuildFailedException, TooManyTeamContextFlagsException
)


class TeamContextBuilder(Builder[TeamContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce TeamContext instances whose integrity is always guaranteed.
     2.  Manage construction of TeamContext instances that can be used safely by the client.
     3.  Ensure params for TeamContext creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
        *   build

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
            player_agent: Optional[PlayerAgent] = None,
            color: Optional[GameColor] = None,
            arena_service: ArenaService = ArenaService(),
            player_agent_service: PlayerAgentService = PlayerAgentService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[TeamContext]:
        """
        # Action:
            1. Confirm that only one in the tuple (id, designation, player_agent, color, team_schema), is not null.
            2. Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3. If all checks pass build the PieceContext in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   designation (Optional[int])
            8   arena (Optional[Arena])
            *   player_agent (Optional[PlayerAgent])
            *   color (Optional[ArenaColor])

        These Parameters must be provided:
            *   arena_service (ArenaService)
            *   agent_certifier (PlayerAgentService)
            *   identity_service (IdentityService)
            *   schema_validator (TeamSchemaValidator)

        # Returns:
        BuildResult[TeamContext] containing either:
            - On success: TeamContext in the payload.
            - On failure: Exception.

        # Raises:
            *   TeamContextBuildFailedException
            *   NoTeamContextFlagsException
            *   TooManyTeamContextFlagsException
        """
        method = "PieceSearchContextBuilder.builder"
        
        try:
            # Get how many optional parameters are not null. One param needs to be not-null
            params = [id, name, arena, player_agent, color]
            param_count = sum(bool(p) for p in params)
            
            # Cannot search for a Schema object if no attribute value is provided for a hit.
            if param_count == 0:
                return BuildResult.failure(
                    NoTeamContextFlagsException(f"{method}:  {NoTeamContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Only one property-value pair is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    TooManyTeamContextFlagsException(f"{method}: {TooManyTeamContextFlagsException}")
                )
            # After the verifying the correct number of flags are set follow the appropriate Schema build flow.
            
            # id flag enabled, build flow.
            if id is not None:
                validation = identity_service.validate_id(candidate=id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id.TeamContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(id=validation.payload))
            
            # designation flag enabled, build flow.
            if name is not None:
                validation = identity_service.validate_name(candidate=name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a designation.TeamContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(name=validation.payload))
            
            # player_agent flag enabled, build flow.
            if player_agent is not None:
                validation = player_agent_service.validator.validate(candidate=player_agent)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a player_agent.TeamContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(player_agent=validation.payload))
            
            # arena flag enabled, build flow.
            if arena is not None:
                validation = arena_service.item_validator.validate(candidate=arena)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a arena.TeamContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(player_agent=validation.payload))
            
            # color flag enabled, build flow.
            if color is not None:
                validation = color_validator.validate(candidate=color)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a color.TeamContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(color=validation.payload))
            
        # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                TeamContextBuildFailedException(
                    ex=ex, message=f"{method}: {TeamContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )