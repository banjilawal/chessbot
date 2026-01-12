# src/chess/snapshot/builder/builder.py

"""
Module: chess.snapshot.builder.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional

from chess.arena import Arena
from chess.team import Team, TeamService
from chess.agent import PlayerAgent, AgentService
from chess.system import BuildResult, Builder, UnhandledRouteException, LoggingLevelRouter, NumberValidator
from chess.game import (
    Game, SnapshotContext, SnapshotContextBuildFailedException, ZeroSnapshotContextFlagsException,
    ExcessiveSnapshotContextFlagsException
)



class SnapshotContextBuilder(Builder[SnapshotContext]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce SnapshotContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of SnapshotContext instances that can be used safely by the client.
    3.  Ensure params for SnapshotContext creation have met the application's safety contract.
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
            game: Optional[Game],
            team: Optional[Team],
            arena: Optional[Arena],
            timestamp: Optional[int],
            player: Optional[PlayerAgent],
            exception: Optional[Exception],
            team_service: TeamService = TeamService(),
            agent_service: AgentService = AgentService(),
            number_validator: NumberValidator = NumberValidator()
    ) -> BuildResult[SnapshotContext]:
        """
        # ACTION:
            1.  Confirm that only one in the (team, owner, timestamp) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a SnapshotContext and send in a BuildResult. Else, return an exception
                in the BuildResult.

        # PARAMETERS:
            Only one these must be provided:
                *   game (Optional[Game])
                *   team (Optional[Team])
                *   arena (Optional[Arena])
                *   timestamp (Optional[int])
                *   exception (Optional[Exception])
                *   owner (Optional[Player])
                
            These Parameters must be provided:
                *   game_service (GameService)
                *   team_service (TeamService)
                *   arena_service (ArenaService)
                *   player_service (AgentService)
                *   identity_service (IdentityService)

        # RETURNS:
        BuildResult[SnapshotContext] containing either:
            - On success: SnapshotContext in the payload.
            - On failure: Exception.

        # RAISES:
            *   ZeroSnapshotContextFlagsException
            *   SnapshotContextBuildFailedException
            *   ExcessiveSnapshotContextFlagsException
        """
        method = "SnapshotContextBuilder.build"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [team, agent, timestamp]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which PlayerAgents match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroSnapshotContextFlagsException(f"{method}: {ZeroSnapshotContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveSnapshotContextFlagsException(f"{method}: {ExcessiveSnapshotContextFlagsException}")
                )
            # After verifying only one Snapshot attribute-value-tuple is enabled, validate it.

            # Build the timestamp SnapshotContext if its flag is enabled.
            if timestamp is not None:
                validation = number_validator.validate(candidate=timestamp)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an timestamp_SnapshotContext in the BuildResult.
                return BuildResult.success(payload=SnapshotContext(timestamp=timestamp))
            
            # Build the agent SnapshotContext if its flag is enabled.
            if agent is not None:
                validation = agent_service.validator.validate(candidate=agent)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an agent_SnapshotContext in the BuildResult.
                return BuildResult.success(payload=SnapshotContext(agent=agent))
            
            # Build the team SnapshotContext if its flag is enabled.
            if team is not None:
                validation = team_service.validator.validate(candidate=team)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a team_SnapshotContext in the BuildResult.
                return BuildResult.success(payload=SnapshotContext(team=team))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            BuildResult.failure(
                UnhandledRouteException(f"{method}: {UnhandledRouteException.DEFAULT_MESSAGE}")
            )
        # Finally, catch any missed exception and wrap A SnapshotContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
               SnapshotContextBuildFailedException(
                    ex=ex, message=f"{method}: {SnapshotContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
