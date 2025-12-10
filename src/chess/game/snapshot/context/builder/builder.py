# src/chess/game/snapshot/context/builder/builder.py

"""
Module: chess.game.snapshot.context.builder.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from typing import Optional

from chess.team import Team, TeamService
from chess.agent import Agent, AgentService
from chess.system import BuildResult, Builder, LoggingLevelRouter, NumberValidator
from chess.game import (
    GameSnapshotContext, GameSnapshotContextBuildFailedException, NoGameSnapshotContextFlagException,
    TooManyGameSnapshotContextFlagsException
)



class GameSnapShotContextBuilder(Builder[GameSnapshotContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce GameSnapshotContext instances whose integrity is always guaranteed.
     2.  Manage construction of GameSnapshotContext instances that can be used safely by the client.
     3.  Ensure params for GameSnapshotContext creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT
         * Builder

     # PROVIDES:
         *   GameSnapshotContextBuilder

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
            agent: Optional[Agent] = None,
            timestamp: Optional[int] = None,
            team_service: TeamService = TeamService(),
            agent_service: AgentService = AgentService(),
            number_validator: NumberValidator = NumberValidator()
    ) -> BuildResult[GameSnapshotContext]:
        """
        # Action:
            1.  Confirm that only one in the (team, agent, timestamp) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success Build an GameSnapshotContext are return in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   team (Optional[Team])
            *   agent (Optional[Agent])
            *   timestamp (Optional[int])

        These Parameters must be provided:
            *   team_service (TeamService)
            *   agent_service (AgentService)
            *   number_validator (NumberValidator)

        # Returns:
        BuildResult[GameSnapshotContext] containing either:
            - On success: GameSnapshotContext in the payload.
            - On failure: Exception.

        # Raises:
            *   GameSnapshotContextBuildFailedException
            *   NoGameSnapshotContextFlagException
            *   TooManyGameSnapshotContextFlagsException
        """
        method = "GameSnapshotContextBuilder.build"
        try:
            # Get how many optional parameters are not null. One param needs to be not-null
            params = [team, agent, timestamp]
            param_count = sum(bool(p) for p in params)
            
            # Cannot search for a Game object if no attribute value is provided for a hit.
            if param_count == 0:
                return BuildResult.failure(
                    NoGameSnapshotContextFlagException(f"{method}: {NoGameSnapshotContextFlagException.DEFAULT_MESSAGE}")
                )
            # Only one param can be used for a searcher. If you need to searcher by multiple params
            # Filter the previous set of matches in a new GameSnapshotFinder with a new context.
            if param_count > 1:
                return BuildResult.failure(
                    TooManyGameSnapshotContextFlagsException(f"{method}: {TooManyGameSnapshotContextFlagsException}")
                )
            
            # After verifying the correct number of flags has been enabled follow the appropriate
            # GameSnapshotContext build flow.
            
            # Timestamp flag enabled, build flow.
            if timestamp is not None:
                validation = number_validator.validate(candidate=timestamp)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a timestamp_game_snapshot_context in the BuildResult.
                return BuildResult.success(payload=GameSnapshotContext(timestamp=timestamp))
            
            # Agent flag enabled, build flow.
            if agent is not None:
                validation = agent_service.validator.validate(candidate=agent)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an agent_game_snapshot_context in the BuildResult.
                return BuildResult.success(payload=GameSnapshotContext(agent=agent))
            
            # Team flag enabled, build flow.
            if team is not None:
                validation = team_service.validator.validate(candidate=team)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an team_game_snapshot_context in the BuildResult.
                return BuildResult.success(payload=GameSnapshotContext(team=team))
        
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # anGameSnapshotContextBuildFailedException. Then send exception chain a BuildResult.failure.
        except Exception as ex:
            return BuildResult.failure(
               GameSnapshotContextBuildFailedException(
                    ex=ex, message=f"{method}: {GameSnapshotContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
