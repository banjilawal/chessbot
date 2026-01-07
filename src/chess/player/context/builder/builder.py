# src/chess/agent/builder/builder.py

"""
Module: chess.agent.builder.builder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional


from chess.game import Game, GameService
from chess.team import Team, TeamService
from chess.system import Builder, BuildResult, UnhandledRouteException, IdentityService, LoggingLevelRouter
from chess.agent import (
    AgentVariety, AgentContext, AgentContextBuildFailedException, ZeroAgentContextFlagsException,
    ExcessiveAgentContextFlagsException
)



class AgentContextBuilder(Builder[AgentContext]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce AgentContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of AgentContext instances that can be used safely by the client.
    3.  Ensure params for AgentContext creation have met the application's safety contract.
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
            team: Optional[Team] = None,
            game: Optional[Game] = None,
            variety: Optional[AgentVariety] = None,
            team_service: TeamService = TeamService(),
            game_service: GameService = GameService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[AgentContext]:
        """
        # ACTION:
            1.  Confirm that only one in the (id, designation, team, game, agent_variety) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a AgentContext and send in a BuildResult. Else, return an exception
                in the BuildResult.

        # PARAMETERS:
            Only one these must be provided:
                *   id (Optional[int])
                *   designation (Optional[str])
                *   team (Optional[Team])
                *   game (Optional[Game])
                *   agent_variety (Optional[AgentVariety])
    
            These Parameters must be provided:
                *   team_service (TeamService)
                *   game_service (GameService)
                *   identity_service (IdentityService)

        # RETURNS:
          BuildResult[AgentContext] containing either:
                - On success: AgentContext in the payload.
                - On failure: Exception.

        # RAISES:
            *   ZeroAgentContextFlagsException
            *   AgentContextBuildFailedException
            *   ExcessiveAgentContextFlagsException
        """
        method = "AgentSearchContextBuilder.builder"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, name, team, game, variety,]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which PlayerAgents match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroAgentContextFlagsException(f"{method}: {ZeroAgentContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveAgentContextFlagsException(f"{method}: {ExcessiveAgentContextFlagsException}")
                )
            # After verifying only one Player attribute-value-tuple is enabled, validate it.
            
            # Build the id AgentContext if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id_AgentContext in the BuildResult.
                return BuildResult.success(AgentContext(id=id))
            
            # Build the name AgentContext if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(name)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a name_AgentContext in the BuildResult.
                return BuildResult.success(AgentContext(name=name))
            
            # Build the team AgentContext if its flag is enabled.
            if team is not None:
                validation = team_service.validator.validate(candidate=team)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a team_AgentContext in the BuildResult.
                return BuildResult.success(AgentContext(team=team))
            
            # Build the game AgentContext if its flag is enabled.
            if game is not None:
                validation = game_service.validator.validate(candidate=game)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a game_AgentContext in the BuildResult.
                return BuildResult.success(AgentContext(game=game))
            
            # Build the agent_variety AgentContext if its flag is enabled.
            if variety is not None:
                if not isinstance(variety, AgentVariety):
                    return BuildResult.failure(
                        TypeError(f"{method}: Expected AgentVariety, got {type(variety).__name__} instead.")
                    )
                # On validation success return a variety_AgentContext in the BuildResult.
                return BuildResult.success(AgentContext(variety=variety))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            BuildResult.failure(
                UnhandledRouteException(f"{method}: {UnhandledRouteException.DEFAULT_MESSAGE}")
            )
        # Finally, catch any missed exception, wrap an AgentContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                AgentContextBuildFailedException(
                    ex=ex, message=f"{method}: {AgentContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )