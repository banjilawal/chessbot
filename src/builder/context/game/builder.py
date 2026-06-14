# src/builder/context/game/builder.py

"""
Module: builder.context.game.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from logic.agent import PlayerAgent, AgentService
from system import Builder, BuildResult, ExecutionRouteException, IdentityService, LoggingLevelRouter
from model.game import (
    GameContext, GameContextBuildException, ZeroGameContextFlagsException, ArenaGameContextFlagsException
)



class GameContextBuilder(Builder[GameContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> BuildResult[Token]

     Super Class:
         Builder
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
        # ACTION:
            1.  Confirm that only one in the (id, owner) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass build a GameContext and send in a BuildResult. Else, return an exception
                in the BuildResult.

        # PARAMETERS:
            Only one these must be provided:
                *   id (Optional[int])
                *   owner (Optional[Player])
    
            These Parameters must be provided:
                *   player_service (AgentService)
                *   identity_service (IdentityService)

        # RETURNS:
        BuildResult[GameContext] containing either:
            - On success: GameContext in the payload.
            - On failure: Exception.

        Raises:
            *   ZeroGameContextFlagsException
            *   GameContextBuildException
            *   ArenaGameContextFlagsException
        """
        method = "GameSearchContextBuilder.build"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, agent,]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which Games match the target.
            if param_count == 0:
                return BuildResult.failure(
                    ZeroGameContextFlagsException(f"{method}: {ZeroGameContextFlagsException.MSG}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return BuildResult.failure(
                    ArenaGameContextFlagsException(f"{method}: {ArenaGameContextFlagsException}")
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
            
            # Build the owner GameContext if its flag is enabled.
            if agent is not None:
                validation = agent_service.validator.search_service(candidate=agent)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return a player_GameContext in the BuildResult.
                return BuildResult.success(GameContext(agent=agent))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the buildResult failure if a map path was missed.
            BuildResult.failure(
                ExecutionRouteException(f"{method}: {ExecutionRouteException.MSG}")
            )
        # Finally, catch any missed exception and wrap A GameContextBuildException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return BuildResult.failure(
                GameContextBuildException(
                    ex=ex, msg=f"{method}: {GameContextBuildException.MSG}"
                )
            )