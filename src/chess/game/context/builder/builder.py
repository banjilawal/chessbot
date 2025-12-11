# src/chess/game/context/builder/builder.py

"""
Module: chess.game.context.builder.builder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional


from chess.agent import Agent, AgentService
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter
from chess.game import (
    GameContext, GameContextBuildFailedException, NoGameContextFlagException, TooManyGameContextFlagsException
)



class GameContextBuilder(Builder[GameContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce GameContext instances whose integrity is always guaranteed.
     2.  Manage construction of GameContext instances that can be used safely by the client.
     3.  Ensure params for GameContext creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
         *   GameContextBuilder

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
            agent: Optional[Agent] = None,
            agent_service: AgentService = AgentService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[GameContext]:
        """
        # Action:
            1.  Confirm that only one in the (id, agent) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success Build an GameContext are return in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   agent (Optional[Agent])

        These Parameters must be provided:
            *   agent_service (AgentService)
            *   identity_service (IdentityService)

        # Returns:
        BuildResult[GameContext] containing either:
            - On success: GameContext in the payload.
            - On failure: Exception.

        # Raises:
            *   GameContextBuildFailedException
            *   NoGameContextFlagException
            *   TooManyGameContextFlagsException
        """
        method = "GameSearchContextBuilder.build"
        try:
            # Get how many optional parameters are not null. One param needs to be not-null
            params = [id, agent,]
            param_count = sum(bool(p) for p in params)
            
            # Cannot search for a Game object if no attribute value is provided for a hit.
            if param_count == 0:
                return BuildResult.failure(
                    NoGameContextFlagException(f"{method}: {NoGameContextFlagException.DEFAULT_MESSAGE}")
                )
            # Only one param can be used for a searcher. If you need to searcher by multiple params
            # Filter the previous set of matches in a new GameSnapshotFinder with a new context.
            if param_count > 1:
                return BuildResult.failure(
                    TooManyGameContextFlagsException(f"{method}: {TooManyGameContextFlagsException}")
                )
            
            # After verifying the correct number of flags has been enabled follow the appropriate
            # GameContext build flow.
            
            # id flag enabled, build flow.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id_game_context in the BuildResult.
                return BuildResult.success(GameContext(id=id))
            
            # Agent flag enabled, build flow.
            if agent is not None:
                validation = agent_service.validator.validate(candidate=agent)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an agent_game_context in the BuildResult.
                return BuildResult.success(GameContext(agent=agent))

        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an GameContextBuildFailedException and send the exception chain a BuildResult.failure.
        except Exception as ex:
            return BuildResult.failure(
                GameContextBuildFailedException(
                    ex=ex, message=f"{method}: {GameContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )