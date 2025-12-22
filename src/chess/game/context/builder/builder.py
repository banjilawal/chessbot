# src/chess/game/map/builder/builder.py

"""
Module: chess.game.map.builder.builder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional


from chess.agent import PlayerAgent, AgentService
from chess.system import Builder, BuildResult, FailsafeBranchExitPointException, IdentityService, LoggingLevelRouter
from chess.game import (
    GameContext, GameContextBuildFailedException, ZeroGameContextFlagsException, ExcessiveGameContextFlagsException
)



class GameContextBuilder(Builder[GameContext]):
    """
    # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce GameContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of GameContext instances that can be used safely by the client.
    3.  Ensure params for GameContext creation have met the application's safety contract.
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
            agent: Optional[PlayerAgent] = None,
            agent_service: AgentService = AgentService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[GameContext]:
        """
        # Action:
            1.  Confirm that only one in the (id, player_agent) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a GameContext and send in a BuildResult. Else, return an exception
                in the BuildResult.

        # Parameters:
            Only one these must be provided:
                *   id (Optional[int])
                *   player_agent (Optional[PlayerAgent])
    
            These Parameters must be provided:
                *   player_agent_service (AgentService)
                *   identity_service (IdentityService)

        # Returns:
        BuildResult[GameContext] containing either:
            - On success: GameContext in the payload.
            - On failure: Exception.

        # Raises:
            *   ZeroGameContextFlagsException
            *   GameContextBuildFailedException
            *   ExcessiveGameContextFlagsException
        """
        method = "GameSearchContextBuilder.build"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, agent,]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which Games match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroGameContextFlagsException(f"{method}: {ZeroGameContextFlagsException.DEFAULT_MESSAGE}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ExcessiveGameContextFlagsException(f"{method}: {ExcessiveGameContextFlagsException}")
                )
            # After verifying only one Board attribute-value-tuple is enabled, validate it.
            
            # id flag enabled, build flow.
            # Build the id GameContext if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return an id_GameContext in the BuildResult.
                return BuildResult.success(GameContext(id=id))
            
            # Build the player_agent GameContext if its flag is enabled.
            if agent is not None:
                validation = agent_service.validator.validate(candidate=agent)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a player_agent_GameContext in the BuildResult.
                return BuildResult.success(GameContext(agent=agent))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            BuildResult.failure(
                FailsafeBranchExitPointException(f"{method}: {FailsafeBranchExitPointException.DEFAULT_MESSAGE}")
            )
        # Finally, catch any missed exception and wrap A GameContextBuildFailedException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                GameContextBuildFailedException(
                    ex=ex, message=f"{method}: {GameContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )