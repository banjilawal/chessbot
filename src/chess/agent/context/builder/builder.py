# src/chess/player_agent/context/builder/builder.py

"""
Module: chess.player_agent.context.builder.builder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional


from chess.game import Game, GameService
from chess.team import Team, TeamService
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter
from chess.agent import (
    AgentVariety, AgentContext, AgentContextBuildFailedException, NoAgentContextFlagException,
    TooManyAgentContextFlagsException
)



class AgentContextBuilder(Builder[AgentContext]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce AgentContext instances whose integrity is always guaranteed.
    2.  Manage construction of AgentContext instances that can be used safely by the client.
    3.  Ensure params for AgentContext creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
        *   Builder

    # PROVIDES:
        *   build:  -> BuildResult[AgentContext]

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
            idservice: IdentityService = IdentityService(),
    ) -> BuildResult[AgentContext]:
        """
        # Action:
            1.  Confirm that only one in the (id, designation, team, game, agent_variety) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success Build an AgentContext are return in a BuildResult.

        # Parameters:
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

        # Returns:
          BuildResult[AgentContext] containing either:
                - On success: AgentContext in the payload.
                - On failure: Exception.

        # Raises:
            *   AgentContextBuildFailedException
            *   NoAgentContextFlagException
            *   TooManyAgentContextFlagsException
        """
        method = "AgentSearchContextBuilder.builder"
        try:
            # Get how many optional parameters are not null. One param is expected to have
            # a value.
            params = [id, name, team, game, variety,]
            param_count = sum(bool(p) for p in params)
            # Cannot searcher for an PlayerAgent object if no attribute value is provided for a hit.
            if param_count == 0:
                return BuildResult.failure(
                    NoAgentContextFlagException(f"{method}: {NoAgentContextFlagException.DEFAULT_MESSAGE}")
                )
            # Only one param can be used for a searcher. If you need to searcher by multiple params
            # Filter the previous set of matches in a new AgentFinder with a new context.
            if param_count > 1:
                return BuildResult.failure(
                    TooManyAgentContextFlagsException(f"{method}: {TooManyAgentContextFlagsException}")
                )
            # After verifying the correct number of switches is turned on validate the target value
            # with the appropriate Validator. On pass create an AgentContext.
            if id is not None:
                validation = idservice.validate_id(id)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(AgentContext(id=id))
            
            if name is not None:
                validation = idservice.validate_name(name)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(AgentContext(name=name))
                
            if team is not None:
                validation = team_service.item_validator.validate(candidate=team)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(AgentContext(team=team))
            
            if game is not None:
                validation = game_service.validate_name(name)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                return BuildResult.success(AgentContext(game=game))
                
            if variety is not None:
                if not isinstance(variety, AgentVariety):
                    return BuildResult.failure(
                        TypeError(f"{method}: Expected AgentVariety, got {type(variety).__name__} instead.")
                    )
                return BuildResult.success(AgentContext(variety=variety))
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an AgentContextBuildFailedException and send the exception chain a BuildResult.failure.
        except Exception as ex:
            return BuildResult.failure(
                AgentContextBuildFailedException(
                    ex=ex, message=f"{method}: {AgentContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )