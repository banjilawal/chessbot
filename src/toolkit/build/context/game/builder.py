# src/integrity/toolkit/context/game/toolkit.py

"""
Module: integrity.toolkit.context.game.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from logic.agent import PlayerAgent, AgentService
from system import Toolkit, ToolkitResult, ExecutionRouteException, IdentityService, LoggingLevelRouter
from model.game import (
    GameContext, GameContextToolkitException, ZeroGameContextFlagsException, ArenaGameContextFlagsException
)



class GameContextToolkit(Toolkit[GameContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Toolkit Process Owner

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
            ) -> ToolkitResult[Token]

     Super Class:
         Toolkit
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def __init__(
            self,
            id: Optional[int] = None,
            agent: Optional[PlayerAgent] = None,
            agent_service: AgentService = AgentService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ToolkitResult[GameContext]:
        """
        # ACTION:
            1.  Confirm that only one in the (id, owner) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass toolkit a GameContext and send in a ToolkitResult. Else, return an exception
                in the ToolkitResult.

        # PARAMETERS:
            Only one these must be provided:
                *   id (Optional[int])
                *   owner (Optional[Player])
    
            These Parameters must be provided:
                *   player_service (AgentService)
                *   identity_service (IdentityService)

        # RETURNS:
        ToolkitResult[GameContext] containing either:
            - On success: GameContext in the payload.
            - On failure: Exception.

        Raises:
            *   ZeroGameContextFlagsException
            *   GameContextToolkitException
            *   ArenaGameContextFlagsException
        """
        method = "GameSearchContextToolkit.toolkit"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, agent,]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which Games match the target.
            if param_count == 0:
                return ToolkitResult.failure(
                    ZeroGameContextFlagsException(f"{method}: {ZeroGameContextFlagsException.MSG}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return ToolkitResult.failure(
                    ArenaGameContextFlagsException(f"{method}: {ArenaGameContextFlagsException}")
                )
            # After verifying only one Board attribute-value-tuple is enabled, validate it.
            
            # id flag enabled, toolkit flow.
            # Toolkit the id GameContext if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return ToolkitResult.failure(validation.exception)
                # On validation success return an id_GameContext in the ToolkitResult.
                return ToolkitResult.success(GameContext(id=id))
            
            # Toolkit the owner GameContext if its flag is enabled.
            if agent is not None:
                validation = agent_service.validator.search_service(candidate=agent)
                if validation.is_failure:
                    return ToolkitResult.failure(validation.exception)
                # On validation success return a player_GameContext in the ToolkitResult.
                return ToolkitResult.success(GameContext(agent=agent))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the toolkitResult failure if a map path was missed.
            ToolkitResult.failure(
                ExecutionRouteException(f"{method}: {ExecutionRouteException.MSG}")
            )
        # Finally, catch any missed exception and wrap A GameContextToolkitException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return ToolkitResult.failure(
                GameContextToolkitException(
                    ex=ex, msg=f"{method}: {GameContextToolkitException.MSG}"
                )
            )