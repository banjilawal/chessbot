# src/chess/team/map/builder/builder.py

"""
Module: chess.team.map.builder.builder
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional


from chess.arena import Arena, ArenaService
from chess.agent import PlayerAgent, AgentService
from chess.system import (
    Builder, BuildResult, FailsafeBranchExitPointException, GameColor, GameColorValidator,
    IdentityService, LoggingLevelRouter
)
from chess.team import (
    NoTeamContextFlagException, TeamContext, TeamContextBuildFailedException, ExcessiveTeamContextFlagsException
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
            player_agent: Optional[PlayerAgent] = None,
            color: Optional[GameColor] = None,
            arena_service: ArenaService = ArenaService(),
            player_agent_service: AgentService = AgentService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> BuildResult[TeamContext]:
        """
        # Action:
            1.  Confirm that only one in the tuple (id, designation, player_agent, color, team_schema), is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a TeamContext and send in a BuildResult. Else, send an exception
                in the BuildResult.

        # Parameters:
            Only one these must be provided:
                *   id (Optional[int])
                *   designation (Optional[int])
                8   arena (Optional[Arena])
                *   player_agent (Optional[PlayerAgent])
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
            params = [id, name, arena, player_agent, color]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which Teams match the target.
            if param_count == 0:
                return BuildResult.failure(
                    NoTeamContextFlagException(f"{method}:  {NoTeamContextFlagException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveTeamContextFlagsException(f"{method}: {ExcessiveTeamContextFlagsException}")
                )
            # After verifying only one Team attribute-value-tuple is enabled, validate it.
            
            # Build the id TeamContext if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(candidate=id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id_TeamContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(id=validation.payload))
            
            # Build the name TeamContext if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(candidate=name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a name_TeamContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(name=validation.payload))
            
            # Build the player_agent TeamContext if its flag is enabled.
            if player_agent is not None:
                validation = player_agent_service.validator.validate(candidate=player_agent)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a player_agent.TeamContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(player_agent=validation.payload))
            
            # Build the arena TeamContext if its flag is enabled.
            if arena is not None:
                validation = arena_service.item_validator.validate(candidate=arena)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an arena_GameContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(player_agent=validation.payload))
            
            # Build the color TeamContext if its flag is enabled.
            if color is not None:
                validation = color_validator.validate(candidate=color)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a color_GameContext in the BuildResult.
                return BuildResult.success(payload=TeamContext(color=validation.payload))
            
            # As a failsafe send a buildResult failure if a map path was missed.
            BuildResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
        # Finally, catch any missed exception, wrap an TeamContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                TeamContextBuildFailedException(
                    ex=ex, message=f"{method}: {TeamContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )