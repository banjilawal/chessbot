# src/chess/game/snapshot/context/builder/builder.py

"""
Module: chess.game.snapshot.context.builder.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from typing import Optional

from chess.team import Team, TeamService
from chess.agent import PlayerAgent, PlayerAgentService
from chess.system import BuildResult, Builder, FailsafeBranchExitPointException, LoggingLevelRouter, NumberValidator
from chess.game import (
    GameSnapshotContext, GameSnapshotContextBuildFailedException, ZeroGameSnapshotContextFlagsException,
    ExcessiveGameSnapshotContextFlagsException
)



class GameSnapShotContextBuilder(Builder[GameSnapshotContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce GameSnapshotContext instances whose integrity is always guaranteed.
     2.  Manage construction of GameSnapshotContext instances that can be used safely by the client.
     3.  Ensure params for GameSnapshotContext creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

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
            team: Optional[Team] = None,
            agent: Optional[PlayerAgent] = None,
            timestamp: Optional[int] = None,
            team_service: TeamService = TeamService(),
            agent_service: PlayerAgentService = PlayerAgentService(),
            number_validator: NumberValidator = NumberValidator()
    ) -> BuildResult[GameSnapshotContext]:
        """
        # Action:
            1.  Confirm that only one in the (team, player_agent, timestamp) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success Build an GameSnapshotContext are return in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   team (Optional[Team])
            *   player_agent (Optional[PlayerAgent])
            *   timestamp (Optional[int])

        These Parameters must be provided:
            *   team_service (TeamService)
            *   player_agent_service (PlayerAgentService)
            *   number_validator (NumberValidator)

        # Returns:
        BuildResult[GameSnapshotContext] containing either:
            - On success: GameSnapshotContext in the payload.
            - On failure: Exception.

        # Raises:
            *   GameSnapshotContextBuildFailedException
            *   ZeroGameSnapshotContextFlagsException
            *   ExcessiveGameSnapshotContextFlagsException
        """
        method = "GameSnapshotContextBuilder.build"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [team, agent, timestamp]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which PlayerAgents match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroGameSnapshotContextFlagsException(f"{method}: {ZeroGameSnapshotContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveGameSnapshotContextFlagsException(f"{method}: {ExcessiveGameSnapshotContextFlagsException}")
                )
            # After verifying only one PlayerAgent attribute-value-tuple is enabled, validate it.
            

            # Build the timestamp GameSnapshotContext if its flag is enabled.
            if timestamp is not None:
                validation = number_validator.validate(candidate=timestamp)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an timestamp_GameSnapshotContext in the BuildResult.
                return BuildResult.success(payload=GameSnapshotContext(timestamp=timestamp))
            
            # PlayerAgent flag enabled, build flow.
            # Build the agent GameSnapshotContext if its flag is enabled.
            if agent is not None:
                validation = agent_service.validator.validate(candidate=agent)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an agent_GameSnapshotContext in the BuildResult.
                return BuildResult.success(payload=GameSnapshotContext(agent=agent))
            
            # Build the team AgentContext if its flag is enabled.
            if team is not None:
                validation = team_service.validator.validate(candidate=team)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a team_GameSnapshotContext in the BuildResult.
                return BuildResult.success(payload=GameSnapshotContext(team=team))
            
            # As a failsafe send a buildResult failure if a context path was missed.
            BuildResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
        
        # Finally, if there is an unhandled exception Wrap an GameSnapshotContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
               GameSnapshotContextBuildFailedException(
                    ex=ex, message=f"{method}: {GameSnapshotContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
